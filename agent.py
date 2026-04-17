"""
Agente de Induccion de IA para la Universidad EIA.
Utiliza Google Gemini API para responder preguntas sobre programas
de bienvenida y servicios estudiantiles.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

class InductionAgent:
    def __init__(self):
        """
        Inicializa el agente de induccion con informacion de la Universidad EIA.
        """
        dotenv_path = Path(__file__).parent / ".env"
        load_dotenv(dotenv_path=dotenv_path)

        # Configurar la API de Gemini desde variables de entorno (archivo .env)
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(
                "Error: Variable de entorno GEMINI_API_KEY no configurada.\n"
                "Crea/edita el archivo .env en esta carpeta con: \n"
                "GEMINI_API_KEY=tu_clave_aqui\n"
                "Puedes crear tu clave en: https://ai.google.dev"
            )

        self.client = genai.Client(api_key=api_key)
        self.model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        
        # Cargar la información de la Universidad
        self.university_info = self._load_university_info()

        # Sesion de chat persistente para memoria conversacional entre turnos
        self.chat_session = None
        
        # Categorías de ayuda disponibles
        self.categories = {
            'desorientación_espacial': ['ubicación', 'dónde', 'bloque', 'edificio', 'oficina', 'mapa', 'camino'],
            'emergencia_médica': ['médico', 'enfermería', 'emergencia', 'herida', 'accidente', 'salud', 'hospital'],
            'deportes': ['deporte', 'fútbol', 'baloncesto', 'voleibol', 'piscina', 'cancha', 'entrenamiento', 'equipo'],
            'alimentación': ['comida', 'almuerzo', 'corredor', 'cafetería', 'comedor', 'menú', 'hambre', 'comer'],
            'académicos': ['clase', 'materia', 'inscripción', 'notas', 'profesor', 'aula', 'calificación', 'estudio', 'retiro'],
            'técnicos': ['wifi', 'plataforma', 'sistemas', 'contraseña', 'correo', 'aula virtual', 'internet', 'soporte'],
            'psicológico': ['psicólogo', 'consejería', 'estrés', 'ansiedad', 'problema', 'conflicto', 'emocional', 'ayuda'],
            'objetos_perdidos': ['perdí', 'perdida', 'extravío', 'objeto', 'hallazgo', 'encontré', 'documento'],
            'profesional': ['práctica', 'empleo', 'carrera', 'profesional', 'trabajo', 'bolsa', 'certificación', 'mentoría'],
            'social_cultura': ['evento', 'actividad', 'club', 'grupo', 'fiesta', 'festival', 'cultural', 'social', 'integración']
        }

        self.system_prompt = self._build_system_prompt()

    def _build_system_prompt(self):
        """
        Construye el contexto de sistema con reglas y base de conocimiento oficial.

        Returns:
            str: Prompt de sistema para Gemini
        """
        return f"""Eres un asistente de inducción amable y profesional de la Universidad EIA en Medellín, Colombia.
                    Tu objetivo es ayudar a estudiantes nuevos con preguntas sobre:
                    - Desorientación espacial (ubicaciones del campus)
                    - Emergencias médicas
                    - Actividades deportivas
                    - Alimentación y servicios de comida
                    - Trámites académicos
                    - Problemas técnicos
                    - Apoyo psicológico
                    - Objetos perdidos
                    - Desarrollo profesional
                    - Vida social y eventos culturales

                    INFORMACIÓN OFICIAL DE LA UNIVERSIDAD:
                    {self.university_info}

                    INSTRUCCIONES:
                    1. Responde de manera amable y profesional en español.
                    2. Basate SIEMPRE en la informacion oficial proporcionada.
                    3. Si la información no está en la base de datos, indícalo claramente.
                    4. Proporciona respuestas concisas pero completas.
                    5. Incluye teléfonos y extensiones cuando sean relevantes.
                    6. Si es una emergencia, destaca los números en **negrita**.
                    7. Sugiere contactos específicos (oficinas o personas) cuando sea necesario.
                    8. Si requiere ubicación, da indicaciones claras con referencias del campus.
                    9. Usa formato estructurado cuando aporte claridad: listas numeradas, viñetas y títulos cortos.
                """

    def _ensure_chat_session(self):
        """
        Crea la sesion de chat de Gemini una sola vez para conservar memoria.
        """
        if self.chat_session is not None:
            return

        self.chat_session = self.client.chats.create(
            model=self.model,
            config={
                "system_instruction": self.system_prompt,
                "temperature": 0.2,
            },
        )

    def _load_university_info(self):
        """
        Carga la información de la universidad desde el archivo .txt
        
        Returns:
            str: Contenido del archivo de información
        """
        info_path = Path(__file__).parent / 'informacion_eia.txt'
        
        try:
            with open(info_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return "Información de Universidad EIA no disponible."
    
    def _categorize_message(self, user_message):
        """
        Categoriza el mensaje del usuario según las palabras clave
        
        Args:
            user_message (str): Mensaje del usuario
            
        Returns:
            str: Categoría identificada o 'general'
        """
        message_lower = user_message.lower()
        
        for category, keywords in self.categories.items():
            if any(keyword in message_lower for keyword in keywords):
                return category
        
        return 'general'

    def process_message(self, user_message):
        """
        Procesa un mensaje del usuario usando Gemini API
        
        Args:
            user_message (str): Mensaje del usuario
            
        Returns:
            str: Respuesta del agente
        """
        try:
            self._ensure_chat_session()

            # Categorizar el mensaje
            category = self._categorize_message(user_message)

            prompt = (
                f"Categoría detectada: {category}\n"
                f"Pregunta del estudiante: {user_message}"
            )

            response = self.chat_session.send_message(prompt)

            assistant_text = response.text or ""
            return assistant_text
        
        except Exception as e:
            error_msg = str(e)
            if "api key" in error_msg.lower() or "authentication" in error_msg.lower() or "permission" in error_msg.lower():
                return (
                    "Error de autenticacion con Gemini API.\n"
                    "Verifica tu clave GEMINI_API_KEY en el archivo .env.\n"
                    "Obten una clave en: https://ai.google.dev"
                )
            if "quota" in error_msg.lower() or "rate limit" in error_msg.lower():
                return (
                    "Se ha alcanzado el limite de solicitudes de la API.\n"
                    "Intenta de nuevo en unos momentos."
                )

            return (
                f"Error al procesar tu pregunta: {error_msg}\n"
                "Intenta nuevamente o contacta a soporte.ti@eia.edu.co"
            )

    def chat(self, user_message):
        """
        Método para obtener respuesta del agente
        
        Args:
            user_message (str): Mensaje del usuario
            
        Returns:
            str: Respuesta del agente
        """
        return self.process_message(user_message)


# Instancia global del agente
agent = InductionAgent()


def get_response(message):
    """
    Función auxiliar para obtener respuesta del agente de inducción
    
    Args:
        message (str): Mensaje del usuario
        
    Returns:
        str: Respuesta del agente
    """
    return agent.chat(message)
