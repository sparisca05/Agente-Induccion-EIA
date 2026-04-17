# Agente de Inducción EIA 🤖

Asistente de IA para la bienvenida de estudiantes nuevos en la Universidad EIA.

## ✨ Características

- **Asistente Inteligente**: Usa Google Gemini API para respuestas contextuales
- **Información Completa**: Base de datos con información oficial de la Universidad EIA
- **Categorización Automática**: Detecta el tipo de pregunta para mejor contexto
- **Interfaz Moderna**: Chat web responsive y atractivo
- **Disponible 24/7**: Acceso web para estudiantes en cualquier momento

## 📋 Temas Cubiertos

1. **Desorientación espacial** - Ubicaciones del campus y edificios
2. **Emergencia médica** - Servicios de salud y primeros auxilios
3. **Interés deportivo** - Programas deportivos y recreación
4. **Alimentación** - Comedor, cafetería y opciones de comida
5. **Trámites académicos** - Inscripción, notas, certificados
6. **Problemas técnicos** - WiFi, plataforma, correo
7. **Apoyo psicológico** - Consejería y apoyo emocional
8. **Objetos perdidos** - Protocolo de búsqueda
9. **Desarrollo profesional** - Prácticas, empleo, certificaciones
10. **Vida social y cultura** - Eventos, clubs, actividades

## 💬 Ejemplos de Preguntas

### Desorientación Espacial
- "¿Dónde está la biblioteca?"
- "¿En qué bloque está la cafetería?"
- "¿Cómo llego a la oficina de admisiones?"

### Emergencia
- "¿Qué hago si tengo una emergencia médica?"
- "¿Dónde está el centro de salud?"

### Deportes
- "¿Qué deportes hay en la Universidad?"
- "¿Cuándo son los entrenamientos de fútbol?"

### Académicos
- "¿Cómo inscribo materias?"
- "¿Dónde veo mis calificaciones?"
- "¿Cuál es el proceso para un retiro?"

### Técnicos
- "¿Cómo me conecto al WiFi?"
- "¿Cuál es mi usuario del aula virtual?"
- "¿A quién contacto por problemas de internet?"

### Psicológico
- "¿Hay servicio de consejería?"
- "¿Cómo solicito apoyo psicológico?"

### Objetos Perdidos
- "Perdí mi carnet, ¿qué hago?"
- "¿Dónde reporto un objeto perdido?"


## Conclusiones

Este proyecto nos permitió validar que un agente conversacional bien contextualizado puede mejorar significativamente la experiencia de inducción de estudiantes nuevos.

### Conclusiones del proyecto

- Centralizar información clave de la Universidad en una base estructurada facilita respuestas más útiles, consistentes y rápidas.
- La categorización automática de preguntas mejora la pertinencia de las respuestas y reduce ambigüedades en consultas frecuentes.
- Una interfaz clara, amigable y responsive aumenta la confianza del usuario y promueve el uso continuo del asistente.
- Integrar un modelo generativo con reglas de contexto institucional fue fundamental para mantener respuestas alineadas con la realidad del campus.

### Aprendizajes como desarrolladores

- Entendimos la importancia de diseñar prompts con objetivos claros, límites y tono adecuado para escenarios educativos.
- Aprendimos a equilibrar creatividad del modelo con control de calidad en las respuestas mediante contexto curado.
- Fortalecimos prácticas de desarrollo colaborativo: organización de archivos, documentación y pruebas funcionales del flujo de chat.
- Confirmamos que la experiencia de usuario no solo depende del backend, sino también de tiempos de respuesta, mensajes de error y claridad visual.

### Retos superados

- Convertimos información institucional extensa en contenido accionable y fácil de consultar por el agente.
- Ajustamos el asistente para responder preguntas variadas (académicas, técnicas, bienestar y vida universitaria) sin perder coherencia.
- Manejamos casos de consultas ambiguas o incompletas, mejorando la robustez de la interacción.
- Diseñamos una solución útil para uso real, con enfoque en acompañamiento, orientación y disponibilidad permanente para estudiantes.


## ⚙️ Configuración Avanzada

### Personalizar el Prompt

Modifica el `system_prompt` en el método `process_message()` de `agent.py` para cambiar el tono o comportamiento del asistente.

### Agregar Más Información

Edita `informacion_eia.txt` para agregar más contenido e información.

### Cambiar el Modelo de Gemini

En el archivo `.env`:
```python
GEMINI_MODEL=gemini-1.5-pro
```


## 🚀 Instalación y Configuración

### 1. Obtener Clave de API de Gemini

1. Ve a [Google AI Studio](https://ai.google.dev)
2. Haz clic en "Get API Key"
3. Crea un nuevo proyecto o selecciona uno existente
4. Copia tu clave API

### 2. Configurar Archivo .env

Edita el archivo `.env` dentro de esta carpeta y pega tu clave:

```env
GEMINI_API_KEY=tu_clave_api_aqui
GEMINI_MODEL=gemini-1.5-flash
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

## ▶️ Ejecutar la Aplicación

```bash
python main.py
```

## 🔧 Archivos Principales

### main.py
- Servidor Flask que sirve la interfaz web
- Endpoint `/api/chat` para procesar mensajes
- Manejo de errores y respuestas JSON

### agent.py
- Clase `InductionAgent` con lógica del asistente
- Integración con Google Gemini API
- Categorización automática de preguntas
- Carga e indexación de información de la Universidad

### index.html
- Interfaz web moderna y responsiva
- Chat con animaciones suaves
- Indicador de escritura
- Compatible con dispositivos móviles

### informacion_eia.txt
- Base de datos completa con:
  - Información general de la Universidad
  - Ubicaciones y mapas del campus
  - Procedimientos y protocolos
  - Horarios y contactos
  - Políticas y normas