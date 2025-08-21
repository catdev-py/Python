-- Orden ascendente
SELECT Nombre, Apellido, Salario FROM Empleados ORDER BY Salario ASC;

-- Orden descendente
SELECT Nombre, Apellido, Salario FROM Empleados ORDER BY Salario DESC;

-- Orden por múltiples columnas
SELECT Nombre, Departamento, Salario FROM Empleados ORDER BY Departamento ASC, Salario DESC;
