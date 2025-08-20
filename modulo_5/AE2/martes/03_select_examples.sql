-- Seleccionar todos los clientes
SELECT * FROM clientes;

-- Seleccionar nombre y correo
SELECT nombre, correo FROM clientes;

-- Filtrar clientes con correo Gmail
SELECT * FROM clientes WHERE correo LIKE '%gmail.com%';

-- Buscar cliente por Primary Key
SELECT * FROM clientes WHERE id = 2;
