-- Tablas base
USE pruebas;
DROP TABLE IF EXISTS ventas_archivo;
DROP TABLE IF EXISTS ventas;

CREATE TABLE ventas (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  fecha      DATE NOT NULL,
  cliente_id INT NOT NULL,
  monto      DECIMAL(12,2) NOT NULL
);

CREATE TABLE ventas_archivo (
  id         INT PRIMARY KEY,  -- conservamos el id original
  fecha      DATE NOT NULL,
  cliente_id INT NOT NULL,
  monto      DECIMAL(12,2) NOT NULL
);

INSERT INTO ventas (fecha, cliente_id, monto) VALUES
('2023-05-10', 10, 12000.00),
('2024-03-15', 11, 18000.00),
('2023-11-20', 12,  9500.00),
('2025-02-01', 13, 25000.00);

-- Procedimiento
DELIMITER $$

DROP PROCEDURE IF EXISTS archivar_ventas_if $$
CREATE PROCEDURE archivar_ventas_if(IN p_fecha DATE)
proc: BEGIN
  DECLARE v_candidatas INT DEFAULT 0;

  START TRANSACTION;

  IF p_fecha IS NULL THEN
    ROLLBACK; SELECT 'ERROR: fecha inválida' AS estado; LEAVE proc;
  END IF;

  SELECT COUNT(*) INTO v_candidatas FROM ventas WHERE fecha < p_fecha;
  IF v_candidatas = 0 THEN
    ROLLBACK; SELECT 'ERROR: no hay ventas para archivar' AS estado; LEAVE proc;
  END IF;

  INSERT INTO ventas_archivo (id, fecha, cliente_id, monto)
  SELECT id, fecha, cliente_id, monto
  FROM ventas
  WHERE fecha < p_fecha;

  DELETE FROM ventas
  WHERE fecha < p_fecha;

  COMMIT;
  SELECT 'OK: ventas archivadas' AS estado, v_candidatas AS cantidad;
END $$
DELIMITER ;

-- Uso:
-- CALL archivar_ventas_if('2024-01-01');
-- SELECT * FROM ventas ORDER BY id;
-- SELECT * FROM ventas_archivo ORDER BY id;
