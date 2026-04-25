# Usamos la version slim ya que la imagen completa pesa mucho mas y no necesitamos todas las herramientas de desarrollo
FROM python:3.12-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Creamos un usuario no root para que el atacante no tenga permisos de root sobre el contenedor
RUN useradd -m appuser

# Instalamos las dependencias necesarias para la aplicación
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la aplicación al contenedor
COPY app.py .

# Cambiamos al usuario no root para la ejecución
USER appuser

# Exponemos el puerto en el que la aplicación va a correr
EXPOSE 5000

# HEALTHCHECK ya que docker detecta y puede reiniciar automáticamente un servicio que dejó de responder. El comando hace una solicitud HTTP al endpoint de salud de la aplicación cada 30 segundos, con un timeout de 10 segundos, y considera el contenedor no saludable después de 3 intentos fallidos.
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/api/health')" || exit 1

# Usamos gunicorn para correr la aplicación en producción, con 4 workers para manejar múltiples solicitudes simultáneamente
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]