USE banco_chile;

START TRANSACTION;

UPDATE cuentas SET saldo = saldo - 350000 WHERE nombre = 'Juan Pérez' AND saldo >= 350000;
UPDATE cuentas SET saldo = saldo + 350000 WHERE nombre = 'Universidad Católica de Temuco';

COMMIT;
