USE banco_chile;

START TRANSACTION;

UPDATE cuentas SET saldo = saldo - 10000 WHERE nombre = 'Juan Pérez' AND saldo >= 10000;
UPDATE cuentas SET saldo = saldo + 10000 WHERE nombre = 'Tarjeta BIP';

COMMIT;
