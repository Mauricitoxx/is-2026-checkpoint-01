from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "activo", 
        "mensaje": "El backend está funcionando correctamente"
    }), 200

@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({
        "servicio": "TeamBoard Backend",
        "version": "1.0.0",
        "lenguaje": "Python 3.12",
        "framework": "Flask"
    }), 200
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)