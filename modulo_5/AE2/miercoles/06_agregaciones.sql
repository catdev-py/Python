-- COUNT empleados
SELECT COUNT(*) AS Total_Empleados FROM Empleados;

-- SUM salarios por departamento
SELECT Departamento, SUM(Salario) AS Total_Salarios FROM Empleados GROUP BY Departamento;

-- AVG salarios por título
SELECT Titulo, AVG(Salario) AS Promedio_Salario FROM Empleados GROUP BY Titulo;
