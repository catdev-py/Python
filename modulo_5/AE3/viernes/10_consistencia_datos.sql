USE banco_chile;

START TRANSACTION;

INSERT INTO cuentas (nombre, saldo) VALUES ('Cliente Inválido', -5000);

ROLLBACK;
