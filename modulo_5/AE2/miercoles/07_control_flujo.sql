-- IF
SELECT Nombre, Apellido, IF(Salario > 2500, 'Alto', 'Normal') AS Categoria_Salario FROM Empleados;

-- CASE
SELECT Nombre, Apellido, Salario,
       CASE 
           WHEN Salario >= 3500 THEN 'Muy Alto'
           WHEN Salario >= 2000 THEN 'Medio'
           ELSE 'Bajo'
       END AS Categoria
FROM Empleados;
