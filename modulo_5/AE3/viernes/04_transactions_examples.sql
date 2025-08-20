-- Ejemplo de Transacciones

-- Crear tabla de cuentas
CREATE TABLE cuentas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    saldo DECIMAL(10,2)
);

-- Insertar datos iniciales
INSERT INTO cuentas (nombre, saldo) VALUES ('Alice', 1000.00), ('Bob', 500.00);

-- Desactivar autocommit y comenzar la transacción
SET autocommit = 0;
START TRANSACTION;

-- Simular transferencia de $200 de Alice a Bob
UPDATE cuentas SET saldo = saldo - 200 WHERE nombre = 'Alice';
UPDATE cuentas SET saldo = saldo + 200 WHERE nombre = 'Bob';

-- Confirmar cambios
COMMIT;

-- O revertir cambios si hay error
-- ROLLBACK;
