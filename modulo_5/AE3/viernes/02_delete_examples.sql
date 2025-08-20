-- Ejemplos de DELETE

-- Eliminar un solo registro
DELETE FROM clientes WHERE id = 5;

-- Eliminar varios registros que cumplan una condición
DELETE FROM productos WHERE stock = 0;

-- Eliminar con múltiples condiciones
DELETE FROM empleados
WHERE departamento = 'Ventas' AND salario < 5000;

-- ⚠️ Eliminar todos los registros de una tabla (peligroso)
-- DELETE FROM usuarios;
