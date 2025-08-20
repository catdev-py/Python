-- Caso práctico de tienda online

-- Tabla de clientes
CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);

-- Tabla de productos
CREATE TABLE productos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    stock INT DEFAULT 10,
    precio DECIMAL(10,2)
);

-- Tabla de ventas
CREATE TABLE ventas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT,
    producto_id INT,
    cantidad INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

-- Insertar datos de prueba
INSERT INTO clientes (nombre, email) VALUES ('Carlos', 'carlos@mail.com'), ('Ana', 'ana@mail.com');
INSERT INTO productos (nombre, stock, precio) VALUES ('Laptop', 5, 1000.00), ('Mouse', 20, 15.00);

-- Actualizar stock de un producto
UPDATE productos SET stock = stock - 1 WHERE id = 1;

-- Eliminar un cliente
DELETE FROM clientes WHERE id = 2;

-- Simular compra con transacción
SET autocommit = 0;
START TRANSACTION;
INSERT INTO ventas (cliente_id, producto_id, cantidad) VALUES (1, 1, 1);
UPDATE productos SET stock = stock - 1 WHERE id = 1;
COMMIT;
