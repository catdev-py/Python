-- Active: 1735145457100@@127.0.0.1@3306@tienda
CREATE DATABASE tienda

USE tienda

CREATE TABLE compras (  
id INTEGER,  
cliente TEXT,  
producto TEXT,  
cantidad INTEGER,  
precio_unitario FLOAT,  
direccion TEXT
);

INSERT INTO compras VALUES 
(1, 'Juan Pérez', 'Laptop', 1, 1000, 'Calle Falsa 123'),
(2, 'Ana García', 'Mouse, Teclado', '2,1', '20,50', 'Av. Siempre Viva');