# 1. Imagen base oficial
FROM python:3.12-slim

# 2. Defino directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copio los archivos index.html y app.js al contenedor
COPY html/

# 4. Expongo puerto que se usará
EXPOSE 8080

# 5. Ejecutar el sevidor de Python
CMD ["python3","-m","http.server", "8080"]