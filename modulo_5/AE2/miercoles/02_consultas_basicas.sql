-- Consultar salarios altos
SELECT Nombre, Apellido, Salario FROM Empleados WHERE Salario > 2500;

-- Consultar salarios bajos
SELECT Nombre, Apellido, Salario FROM Empleados WHERE Salario <= 1800;

-- Promedio de salarios por departamento
SELECT Departamento, AVG(Salario) AS Promedio_Salario FROM Empleados GROUP BY Departamento;
