-- Active: 1735145457100@@127.0.0.1@3306
-- Caso práctico: Veterinaria
CREATE DATABASE veterinaria;
USE veterinaria;

CREATE TABLE duenos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20)
);

CREATE TABLE animales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    especie VARCHAR(50) NOT NULL,
    edad INT,
    peso DECIMAL(5,2),
    dueno_id INT,
    FOREIGN KEY (dueno_id) REFERENCES duenos(id)
);

-- Insertar datos de prueba
INSERT INTO duenos (nombre, telefono) VALUES ('Juan Pérez', '987654321');
INSERT INTO animales (nombre, especie, edad, peso, dueno_id)
VALUES ('Firulais', 'Perro', 3, 12.5, 1);
