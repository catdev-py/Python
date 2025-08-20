-- Selecciona la base de datos (ajusta según corresponda)
USE mydb;

-- Eliminar tablas si existen
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS usuarios;

-- Ejemplos de Restricciones

CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    edad INT CHECK (edad >= 18)
);

CREATE TABLE pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    producto VARCHAR(100) NOT NULL,
    cantidad INT DEFAULT 1,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
