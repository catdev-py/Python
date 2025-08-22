CREATE DATABASE banco_chile;
USE banco_chile;

CREATE TABLE cuentas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    saldo DECIMAL(10,2) NOT NULL CHECK (saldo >= 0)
) ENGINE=InnoDB;

INSERT INTO cuentas (nombre, saldo) VALUES
('Juan Pérez', 150000),
('María González', 80000);
