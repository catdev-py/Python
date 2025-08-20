-- Caso práctico de tienda
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2)
);

CREATE TABLE ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT,
    cantidad INT,
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

-- Insertar productos y ventas
INSERT INTO productos (nombre, precio)
VALUES ('Laptop', 1200), ('Mouse', 25);

INSERT INTO ventas (producto_id, cantidad)
VALUES (1, 2), (2, 5);

-- Actualizar precio de un producto
UPDATE productos SET precio = 1100 WHERE id = 1;

-- Eliminar una venta
DELETE FROM ventas WHERE id = 2;
