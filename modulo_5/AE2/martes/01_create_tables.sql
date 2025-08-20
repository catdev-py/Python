-- Active: 1735145457100@@127.0.0.1@3306@bootcamp_db
CREATE DATABASE IF NOT EXISTS bootcamp_db;
USE bootcamp_db;

CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100)
);

CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    cliente_id INT,
    producto VARCHAR(100),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
