USE banco_chile;

START TRANSACTION;

UPDATE cuentas SET saldo = saldo - 50000 WHERE nombre = 'Juan Pérez';
UPDATE cuentas SET saldo = saldo + 50000 WHERE nombre = 'María González';

COMMIT;
