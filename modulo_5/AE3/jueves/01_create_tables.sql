CREATE DATABASE IF NOT EXISTS bootcamp_db3;
USE bootcamp_db3;

CREATE TABLE departamentos (
    id_departamento INT PRIMARY KEY,
    nombre_departamento VARCHAR(100)
);

CREATE TABLE empleados (
    id_empleado INT PRIMARY KEY,
    nombre VARCHAR(100),
    salario DECIMAL(10,2),
    id_departamento INT,
    FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento)
);
