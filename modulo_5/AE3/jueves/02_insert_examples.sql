-- Insertar datos en departamentos
INSERT INTO departamentos (id_departamento, nombre_departamento)
VALUES (1, 'Recursos Humanos'), (2, 'TI');

-- Insertar empleados referenciando a departamentos
INSERT INTO empleados (id_empleado, nombre, salario, id_departamento)
VALUES (101, 'Juan Pérez', 3500, 1),
       (102, 'Ana Gómez', 4200, 2);
