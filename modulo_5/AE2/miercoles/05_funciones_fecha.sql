-- Fecha y hora actual
SELECT NOW() AS Fecha_Hora_Actual;

-- Solo fecha actual
SELECT CURDATE() AS Fecha_Actual;

-- Año, Mes, Día
SELECT YEAR(NOW()) AS Anio, MONTH(NOW()) AS Mes, DAY(NOW()) AS Dia;

-- Cambiar formato de fecha
SELECT DATE_FORMAT(NOW(), '%d/%m/%Y %H:%i:%s') AS Fecha_Formateada;
