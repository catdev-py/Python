-- Ejemplo con AUTO_INCREMENT
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100)
);

INSERT INTO clientes (nombre, correo)
VALUES ('Pedro', 'pedro@gmail.com'), ('Lucía', 'lucia@yahoo.com');
