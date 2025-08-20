-- Ordenar por salario descendente
SELECT nombre, salario FROM empleados ORDER BY salario DESC;

-- Ordenar por departamento y luego salario
SELECT nombre, departamento, salario
FROM empleados
ORDER BY departamento ASC, salario DESC;
