USE banco_chile;

SET autocommit = 1;
UPDATE cuentas SET saldo = saldo + 10000 WHERE nombre = 'María González';

SET autocommit = 0;
UPDATE cuentas SET saldo = saldo + 5000 WHERE nombre = 'María González';
ROLLBACK;
