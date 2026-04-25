import os
import psycopg2
from psycopg2.extras import RealDictCursor #las consultas a la base de datos se devuelven como diccionarios.
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "activo", 
        "mensaje": "El backend está funcionando correctamente"
    }), 200

@app.route('/api/team', methods=['GET'])
def get_team():
    try:
        host = os.environ.get('DB_HOST', 'database') 
        port = os.environ.get('DB_PORT', '5432')
        user = os.environ.get('DB_USER', 'postgres')
        password = os.environ.get('DB_PASSWORD', 'postgres')
        dbname = os.environ.get('DB_NAME', 'teamboard_db')

        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            dbname=dbname
        )
        
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM members;")
        members = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(members), 200

    except Exception as e:
        return jsonify({"error": "Error al conectar con la base de datos", "detalle": str(e)}), 500


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