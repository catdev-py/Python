-- Agrupar empleados por departamento
SELECT departamento, COUNT(*) AS total
FROM empleados
GROUP BY departamento;

-- Promedio de salarios por departamento
SELECT departamento, AVG(salario) AS promedio
FROM empleados
GROUP BY departamento;
