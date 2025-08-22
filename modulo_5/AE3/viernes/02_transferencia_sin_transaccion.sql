USE banco_chile;

UPDATE cuentas SET saldo = saldo - 50000 WHERE nombre = 'Juan Pérez';
UPDATE cuentas SET saldo = saldo + 50000 WHERE nombre = 'María González';
