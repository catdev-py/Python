USE banco_chile;

START TRANSACTION;

UPDATE cuentas SET saldo = saldo - 200000 WHERE nombre = 'María González';
-- Simulación de error
ROLLBACK;
