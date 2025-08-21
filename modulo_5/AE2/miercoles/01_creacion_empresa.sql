-- Crear la base de datos y tabla
CREATE DATABASE IF NOT EXISTS Empresa;
USE Empresa;

CREATE TABLE Empleados (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Direccion VARCHAR(100),
    Ciudad VARCHAR(50),
    Telefono VARCHAR(20),
    Salario DECIMAL(10,2),
    Departamento VARCHAR(50),
    Titulo VARCHAR(50)
);

-- Insertar registros de ejemplo
INSERT INTO Empleados (Nombre, Apellido, Direccion, Ciudad, Telefono, Salario, Departamento, Titulo)
VALUES
('Ana', 'Pérez', 'Calle 123', 'Santiago', '987654321', 1500.00, 'Ventas', 'Vendedor'),
('Luis', 'Gómez', 'Av. Central 456', 'Santiago', '912345678', 2200.00, 'Ventas', 'Supervisor'),
('Carla', 'Rojas', 'Calle Norte 789', 'Concepción', '923456789', 1800.00, 'Ventas', 'Vendedor'),
('Pedro', 'Fernández', 'Pasaje Sur 101', 'Valparaíso', '934567890', 3000.00, 'TI', 'Ingeniero de Software'),
('María', 'López', 'Av. Principal 202', 'Santiago', '945678901', 2800.00, 'TI', 'Ingeniero de Software'),
('Jorge', 'Soto', 'Calle 5 Oriente', 'Concepción', '956789012', 3500.00, 'TI', 'Jefe de Proyecto'),
('Camila', 'Torres', 'Av. Libertad 303', 'Temuco', '967890123', 1700.00, 'Recursos Humanos', 'Asistente'),
('Andrés', 'Molina', 'Calle Sur 404', 'Valparaíso', '978901234', 2500.00, 'Recursos Humanos', 'Analista'),
('Sofía', 'Reyes', 'Av. Norte 505', 'Santiago', '989012345', 4000.00, 'Gerencia', 'Gerente General'),
('Ricardo', 'Vargas', 'Calle Central 606', 'Temuco', '990123456', 1200.00, 'Ventas', 'Practicante');
