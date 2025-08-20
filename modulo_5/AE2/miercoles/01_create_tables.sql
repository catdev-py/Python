CREATE DATABASE IF NOT EXISTS bootcamp_db2;
USE bootcamp_db2;

CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    departamento VARCHAR(50),
    salario DECIMAL(10,2),
    fecha_contratacion DATE
);

INSERT INTO empleados VALUES
(1, 'Ana', 'Lopez', 'HR', 2500, '2020-01-10'),
(2, 'Pedro', 'Gomez', 'IT', 3200, '2019-03-15'),
(3, 'Lucía', 'Martinez', 'HR', 2800, '2021-07-20'),
(4, 'Carlos', 'Perez', 'IT', 4000, '2018-11-05');
