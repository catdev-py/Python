-- Active: 1735145457100@@127.0.0.1@3306@banco_chile
-- Ejemplos de UPDATE

-- Actualizar un campo específico
UPDATE clientes
SET telefono = '555-1234'
WHERE id = 3;

-- Actualizar varios campos
UPDATE productos
SET precio = 19.99, stock = 50
WHERE id = 8;

-- Actualización masiva con condición
UPDATE empleados
SET salario = salario * 1.10
WHERE departamento = 'Ventas';

-- ⚠️ Actualización sin WHERE (peligroso)
-- UPDATE usuarios SET estado = 'inactivo';

-- Actualización con múltiples condiciones
UPDATE estudiantes
SET promedio = 9.5
WHERE grado = 3 AND grupo = 'B';
