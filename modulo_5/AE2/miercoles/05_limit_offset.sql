-- Limitar resultados
SELECT * FROM empleados LIMIT 2;

-- Paginación con LIMIT y OFFSET
SELECT * FROM empleados ORDER BY nombre LIMIT 2 OFFSET 2;
