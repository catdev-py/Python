-- Agrupar por departamento
SELECT Departamento, COUNT(*) AS Total FROM Empleados GROUP BY Departamento;

-- Agrupar por título y departamento
SELECT Departamento, Titulo, COUNT(*) AS Total FROM Empleados GROUP BY Departamento, Titulo;
