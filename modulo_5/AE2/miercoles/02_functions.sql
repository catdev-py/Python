-- Funciones de texto
SELECT CONCAT(nombre, ' ', apellido) AS nombre_completo FROM empleados;

-- Funciones numéricas
SELECT AVG(salario) AS promedio_salario FROM empleados;

-- Funciones de fecha
SELECT nombre, YEAR(fecha_contratacion) AS anio FROM empleados;
