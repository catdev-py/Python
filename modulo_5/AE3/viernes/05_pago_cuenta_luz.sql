USE banco_chile;

START TRANSACTION;

UPDATE cuentas
SET saldo = saldo - 25000
WHERE nombre = 'Juan Pérez' AND saldo >= 25000;

SET @filas_afectadas = ROW_COUNT();

COMMIT;
ROLLBACK;
END IF;
