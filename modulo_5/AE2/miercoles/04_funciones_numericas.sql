-- SUM
SELECT SUM(Salario) AS Total_Salarios FROM Empleados;

-- AVG
SELECT AVG(Salario) AS Promedio_Salario FROM Empleados;

-- MAX y MIN
SELECT MAX(Salario) AS Salario_Maximo, MIN(Salario) AS Salario_Minimo FROM Empleados;

-- ROUND
SELECT Nombre, ROUND(Salario, 0) AS Salario_Redondeado FROM Empleados;
