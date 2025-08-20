-- Ejemplo de transacciones
START TRANSACTION;

INSERT INTO empleados (id_empleado, nombre, salario, id_departamento)
VALUES (103, 'Carlos Ruiz', 3900, 1);

UPDATE empleados SET salario = salario + 200 WHERE id_empleado = 103;

-- Si todo está bien, confirmamos:
COMMIT;

-- Si hubo un error, podríamos usar:
-- ROLLBACK;
