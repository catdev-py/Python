USE banco_chile;

START TRANSACTION;

UPDATE cuentas
SET saldo = saldo - 25000
WHERE nombre = 'Juan Pérez' AND saldo >= 25000;

SELECT ROW_COUNT() INTO @filas_afectadas;

IF @filas_afectadas > 0 THEN
    INSERT INTO cuentas (nombre, saldo) VALUES ('ENEL Chile', 25000);
    COMMIT;
ELSE
    ROLLBACK;
END IF;
