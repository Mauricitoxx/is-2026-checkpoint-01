## Feature 05 - Portainer

Utilizamos Portainer CE como panel web de monitoreo y administración de contenedores docker del proyecto. Esta herramienta permite gestionar la infraestructura desde una interfaz gráfica, sin depender exclusivamente de la terminal.

### Configuración

El servicio fue configurado en el docker-compose.yml utilizando la imagen:
    `portainer/portainer-ce:latest`

Se monto el socket docker para conectarse al motor docker del host:
    `/var/run/docker.sock:/var/run/docker.sock`

Se configuro un volumen persistente para poder conservar usuarios y configuraciones:
    `portainer-data:/data`

### Acceso

Inicializando el proyecto con:
    `docker compose up -d`

Se accede desde el navegador:
    `http://localhost:9000`

En el primer acceso se solicitó crear un usuario administrador.

### Verificaciones realizadas

    Visualización de contenedores del sistema.
![Contenedores](portainer/screenshots/contenedores.jpeg)

    Visualización de redes Docker.
![Redes](portainer/screenshots/networks.jpeg)
    
    Visualización de volúmenes persistentes.
![Volúmenes](portainer/screenshots/volumes.jpeg)
    
    Administración desde interfaz web.
![Dashboard](portainer/screenshots/dashboard.jpeg)