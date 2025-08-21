-- Concatenar nombre y apellido
SELECT CONCAT(Nombre, ' ', Apellido) AS Nombre_Completo FROM Empleados;

-- Mayúsculas
SELECT UPPER(Nombre) AS Nombre_Mayuscula FROM Empleados;

-- Minúsculas
SELECT LOWER(Apellido) AS Apellido_Minuscula FROM Empleados;

-- Largo de texto
SELECT Nombre, LENGTH(Nombre) AS Largo_Nombre FROM Empleados;

-- Substring
SELECT Apellido, SUBSTRING(Apellido, 1, 3) AS Iniciales FROM Empleados;
