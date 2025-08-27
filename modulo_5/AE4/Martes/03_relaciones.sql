-- Crear tabla clases con claves foráneas
CREATE TABLE clases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    profesor_id INT,
    estudiante_id INT,
    FOREIGN KEY (profesor_id) REFERENCES profesores(id),
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id)
);
