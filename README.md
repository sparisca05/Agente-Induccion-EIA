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

## 🚢 Despliegue con Servidor WSGI (Producción)

Para producción no uses `python main.py` porque ese comando levanta el servidor de desarrollo de Flask.

### Opción recomendada en Windows: Waitress

1. Instala dependencias (incluye Waitress):

```bash
pip install -r requirements.txt
```

2. Ejecuta el servidor WSGI:

```bash
python -m waitress --host=0.0.0.0 --port=5000 wsgi:application
```

La app quedará disponible en `http://localhost:5000`.

### Opción común en Linux: Gunicorn

Si despliegas en Linux, puedes usar:

```bash
gunicorn --workers 2 --bind 0.0.0.0:5000 wsgi:application
```

> Nota: Gunicorn no es la opción ideal para Windows nativo.

Verás un mensaje como:
```
🚀 Servidor iniciado en http://localhost:5000
📱 Abre tu navegador y ve a http://localhost:5000
⚠️  Presiona Ctrl+C para detener el servidor
```

### Abrir en el Navegador

Abre tu navegador y ve a:
```
http://localhost:5000
```

## 📁 Estructura de Archivos

```
Agente Induccion/
├── main.py                    # Servidor Flask
├── agent.py                   # Lógica del agente con Gemini
├── index.html                 # Interfaz web del chat
├── informacion_eia.txt        # Base de datos de la Universidad
├── requirements.txt           # Dependencias Python
└── README.md                  # Este archivo
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

## ⚙️ Configuración Avanzada

### Cambiar el Modelo de Gemini

En el archivo `.env`:
```python
GEMINI_MODEL=gemini-1.5-pro
```

### Personalizar el Prompt

Mostifica el `system_prompt` en el método `process_message()` de `agent.py` para cambiar el tono o comportamiento del asistente.

### Agregar Más Información

Edita `informacion_eia.txt` para agregar más contenido e información.

## 🐛 Solución de Problemas

### Error: "GEMINI_API_KEY not found"
- Verifica que configuraste la variable de entorno
- Reinicia la terminal después de establecer la variable
- Usa `echo %GEMINI_API_KEY%` (Windows) para verificar

### Error: "Module not found"
- Asegúrate de instalar las dependencias: `pip install -r requirements.txt`
- Verifica que estés en el directorio correcto

### Servidor no responde
- Verifica que estés usando `http://localhost:5000` (no `https`)
- Comprueba que el puerto 5000 esté disponible
- Revisa la consola para mensajes de error

### Respuestas lentas
- Es normal con Gemini API, espera 2-3 segundos
- Verifica tu conexión a internet
- Comprueba que tu cuota de API no esté agotada

## 📊 Límites de la API

- **Free Tier**: 60 solicitudes por minuto
- **Limite de caracteres**: 32,000 caracteres por solicitud
- Para límites más altos, consulta [Google AI Studio](https://ai.google.dev)

## 🔐 Seguridad

⚠️ **IMPORTANTE**: Nunca compartas tu clave API de Gemini
- No la incluyas en repositorios de Git
- No la muestres en código fuente
- Usa variables de entorno siempre

## 📞 Soporte

Si encuentras problemas:
1. Revisa la consola para mensajes de error
2. Verifica la configuración de GEMINI_API_KEY
3. Intenta actualizar las dependencias
4. Contacta a soporte.ti@eia.edu.co

## 📝 Licencia

Desarrollado para la Universidad EIA

## 👨‍💻 Contribuciones

Para mejorar el agente:
1. Actualiza `informacion_eia.txt` con información faltante
2. Personaliza `agent.py` con lógica adicional
3. Mejora la interfaz en `index.html`
4. Proporciona feedback sobre las respuestas

---

**¡Bienvenido a EIA! 🎓**
