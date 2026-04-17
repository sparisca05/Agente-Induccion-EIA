"""
Servidor Flask para la interfaz web del chat con agente IA
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from agent import get_response
import os

app = Flask(__name__, 
            template_folder=os.path.dirname(os.path.abspath(__file__)),
            static_folder=os.path.dirname(os.path.abspath(__file__)))

# Habilitar CORS
CORS(app)

# Ruta para servir la página principal
@app.route('/')
def index():
    """Página principal del chat"""
    return render_template('index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Endpoint para procesar mensajes del chat
    
    Espera JSON con:
    {
        "message": "texto del usuario"
    }
    
    Retorna:
    {
        "reply": "respuesta del agente"
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({'error': 'Mensaje no proporcionado'}), 400
        
        user_message = data['message'].strip()
        
        if not user_message:
            return jsonify({'error': 'Mensaje vacío'}), 400
        
        # Obtener respuesta del agente
        response = get_response(user_message)
        
        return jsonify({'reply': response}), 200
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Error al procesar el mensaje'}), 500


@app.route('/api/health', methods=['GET'])
def health():
    """Verificar que el servidor está activo"""
    return jsonify({'status': 'ok'}), 200


if __name__ == '__main__':
    # Ejecutar el servidor
    print("🚀 Servidor iniciado en http://localhost:5000")
    print("📱 Abre tu navegador y ve a http://localhost:5000")
    print("⚠️  Presiona Ctrl+C para detener el servidor\n")
    
    app.run(
        debug=True,
        host='localhost',
        port=5000
    )
