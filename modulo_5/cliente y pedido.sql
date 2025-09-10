
USE pruebas;
-- Tablas base
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS clientes;
CREATE TABLE clientes (
  id     INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  email  VARCHAR(150) UNIQUE
);
CREATE TABLE pedidos (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  cliente_id INT NOT NULL,
  fecha      DATE NOT NULL,
  total      DECIMAL(12,2) NOT NULL,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
INSERT INTO clientes (nombre, email) VALUES
('Juan Soto', 'juan@example.com');
-- Procedimiento
DELIMITER $$
DROP PROCEDURE IF EXISTS crear_cliente_pedido_if $$
CREATE PROCEDURE crear_cliente_pedido_if(IN p_nombre VARCHAR(100),IN p_email  VARCHAR(150),IN p_total  DECIMAL(12,2))
proc: BEGIN
  DECLARE v_dup INT DEFAULT 0;
  DECLARE v_cliente_id INT;

  START TRANSACTION;

  IF p_nombre IS NULL OR p_email IS NULL OR p_total IS NULL OR p_total <= 0 THEN
    ROLLBACK; SELECT 'ERROR: datos inválidos' AS estado; LEAVE proc;
  END IF;

  SELECT COUNT(*) INTO v_dup FROM clientes WHERE email = p_email;
  IF v_dup > 0 THEN
    ROLLBACK; SELECT 'ERROR: email ya existe' AS estado; LEAVE proc;
  END IF;

  INSERT INTO clientes (nombre, email) VALUES (p_nombre, p_email);
  SET v_cliente_id = LAST_INSERT_ID();

  INSERT INTO pedidos (cliente_id, fecha, total)
  VALUES (v_cliente_id, CURDATE(), p_total);

  COMMIT;
  SELECT 'OK: cliente y pedido creados' AS estado, v_cliente_id AS cliente_id;
END $$
DELIMITER ;

-- Uso:
CALL crear_cliente_pedido_if('Ana Pérez','ana.perez@example.com', 29990);
SELECT c.*, p.* FROM clientes c LEFT JOIN pedidos p ON p.cliente_id=c.id ORDER BY c.id, p.id;

