CREATE TABLE IF NOT EXISTS members (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    legajo VARCHAR(50),
    feature VARCHAR(100),
    servicio VARCHAR(100),
    estado VARCHAR(50)
);

INSERT INTO members (nombre, apellido, legajo, feature, servicio, estado) VALUES
('Mauro', 'Lista', '32042', 'Feature 01', 'Coordinador', 'Running'),
('Oriana', 'Acosta', '32671', 'Feature 04', 'PostgreSQL', 'Running'),
('Juan Cruz ', 'Caceres', '33168', 'Feature 02', 'Fronted', 'Running'),
('Thiago ', 'Perez', '32307', 'Feature 03', 'Backend', 'Running'),
('Iara', 'Rearte', '33433', 'Feature 05', 'Portainer', 'Running');
