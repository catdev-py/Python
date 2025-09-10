CREATE DATABASE Alquiler_autos;
use Alquiler_autos;

CREATE TABLE Clientes (
  id_cliente INT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  telefono VARCHAR(50),
  email VARCHAR(150),
  direccion VARCHAR(200)
);

CREATE TABLE Vehiculos (
  id_vehiculo INT PRIMARY KEY,
  marca VARCHAR(50) NOT NULL,
  modelo VARCHAR(50) NOT NULL,
  anio INT NOT NULL,
  precio_dia DECIMAL(10, 2) NOT NULL
);

CREATE TABLE alquileres (
  id_alquiler INT PRIMARY KEY,
  id_cliente INT NOT NULL,
  id_vehiculo INT NOT NULL,
  fecha_inicio DATE NOT NULL,
  fecha_fin DATE NOT NULL,
  FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
  FOREIGN KEY (id_vehiculo) REFERENCES Vehiculos(id_vehiculo)
);

CREATE TABLE Pagos (
  id_pago INT PRIMARY KEY,
  id_alquiler INT NOT NULL,
  monto DECIMAL(10, 2) NOT NULL,
  fecha_pago DATE NOT NULL,
  FOREIGN KEY (id_alquiler) REFERENCES alquileres(id_alquiler)
);

INSERT INTO Clientes (id_cliente, nombre, telefono, email, direccion) VALUES
(1, 'Juan Perez', '555-1234', 'juan@mail.com', 'Calle 123'),
(2, 'Laura Gomez', '555-5678','laura@mail.com', 'Calle 456'),
(3, 'Carlos Sanchez', '555-9101', 'carlos@mail.com', 'Calle 789'),
(4, 'Ana Martinez', '555-1122', 'ana@mail.com', 'Calle 321'),
(5, 'Luis Rodriguez', '555-3344', 'luis@mail.com', 'Calle 654');

INSERT INTO Vehiculos (id_vehiculo, marca, modelo, anio, precio_dia) VALUES
(1, 'Toyota', 'Corolla', 2020, 30.00),
(2, 'Honda', 'Civic', 2019, 28.00),
(3, 'Ford', 'Focus', 2021, 35.00);

INSERT INTO Alquileres (id_alquiler, id_cliente, id_vehiculo, fecha_inicio, fecha_fin) VALUES
(1, 1, 2, '2025-03-10', '2025-03-15'),
(2, 2, 1, '2025-03-12', '2025-03-16'),
(3, 3, 3, '2025-03-20', '2025-03-22');

INSERT INTO Pagos (id_pago, id_alquiler, monto, fecha_pago) VALUES
(1, 1, 150.00, '2025-03-12'),
(2, 2, 112.00, '2025-03-13'),
(3, 3, 70.00, '2025-03-20');

-- COMMENT 1. Muestra el nombre, telefono y email de los clientes que tienen un alquiler activo en una fecha dada (2025-03-13).
SELECT clientes.nombre, clientes.telefono, clientes.email
FROM clientes 
JOIN alquileres ON clientes.id_cliente = alquileres.id_cliente
WHERE '2025-03-13' BETWEEN alquileres.fecha_inicio AND alquileres.fecha_fin;

-- COMMENT 2. Muestra la marca, modelo y precio por día de los vehículos que están alquilados en el mes de marzo de 2025.
SELECT vehiculos.marca, vehiculos.modelo, vehiculos.precio_dia
FROM vehiculos
JOIN alquileres ON vehiculos.id_vehiculo = alquileres.id_vehiculo
WHERE MONTH(alquileres.fecha_inicio) = 3 AND YEAR(alquileres.fecha_inicio) = 2025;

-- COMMENT 3. Muestra el precio total pagado por cada alquiler, junto con el nombre del cliente y la marca del vehículo.
SELECT clientes.nombre, vehiculos.marca, pagos.monto
FROM pagos
JOIN alquileres ON pagos.id_alquiler = alquileres.id_alquiler
JOIN clientes ON alquileres.id_cliente = clientes.id_cliente
JOIN vehiculos ON alquileres.id_vehiculo = vehiculos.id_vehiculo;

-- COMMENT 4. Se muestra el nombre e email de los clientes que no han realizado ningún pago.
SELECT clientes.nombre, clientes.email
FROM clientes
LEFT JOIN pagos ON clientes.id_cliente = pagos.id_alquiler
WHERE pagos.id_alquiler IS NULL;

-- COMMENT 5. Se muestra el nombre del cliente y el promedio de pagos realizados por cada cliente.
SELECT clientes.nombre, AVG(pagos.monto) AS promedio_pagos
FROM clientes
JOIN pagos ON clientes.id_cliente = pagos.id_alquiler
GROUP BY clientes.id_cliente;

-- COMMENT 6. Se muestra el modelo, marca y precio del dia de los vehículos que no han sido alquilados el 12 de marzo de 2025.
SELECT vehiculos.modelo, vehiculos.marca, vehiculos.precio_dia
FROM vehiculos
LEFT JOIN alquileres ON vehiculos.id_vehiculo = alquileres.id_vehiculo
  AND '2025-03-12' BETWEEN alquileres.fecha_inicio AND alquileres.fecha_fin
WHERE alquileres.id_vehiculo IS NULL;

-- COMMENT 7. Se muestra la marca y el modelo de los vehículos que han sido alquilados más de una vez en el mes de marzo de 2025.
SELECT vehiculos.marca, vehiculos.modelo
FROM vehiculos
JOIN alquileres ON vehiculos.id_vehiculo = alquileres.id_vehiculo
WHERE MONTH(alquileres.fecha_inicio) = 3 AND YEAR(alquileres.fecha_inicio) = 2025
GROUP BY vehiculos.id_vehiculo
HAVING COUNT(*) > 1;

-- COMMENT 8. Se muestra el nombre del cliente y la cantidad total pagada por cada cliente que ha realizado pagos.  
SELECT clientes.nombre, SUM(pagos.monto) AS total_pagado
FROM clientes
JOIN pagos ON clientes.id_cliente = pagos.id_alquiler
GROUP BY clientes.id_cliente;

-- COMMENT 9. Se muestra el nombre del cliente y la fecha de alquiler de quienes alquilaron un vehículo ford focus.
SELECT clientes.nombre, alquileres.fecha_inicio, alquileres.fecha_fin
FROM clientes
JOIN alquileres ON clientes.id_cliente = alquileres.id_cliente
JOIN vehiculos ON alquileres.id_vehiculo = vehiculos.id_vehiculo
WHERE vehiculos.marca = 'Ford' AND vehiculos.modelo = 'Focus';

-- COMMENT 10. Se muestra el nombre del cliente, la marca del vehículo y la duración del alquiler en días de menor a mayor para todos los alquileres realizados. COMMENT
SELECT clientes.nombre, vehiculos.marca, DATEDIFF(alquileres.fecha_fin, alquileres.fecha_inicio) AS duracion_dias
FROM alquileres
JOIN clientes ON alquileres.id_cliente = clientes.id_cliente
JOIN vehiculos ON alquileres.id_vehiculo = vehiculos.id_vehiculo
ORDER BY duracion_dias ASC;