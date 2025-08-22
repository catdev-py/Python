USE banco_chile;

START TRANSACTION;

UPDATE cuentas SET saldo = saldo - 45000 WHERE nombre = 'María González' AND saldo >= 45000;

SELECT ROW_COUNT() INTO @afectado;

IF @afectado > 0 THEN
    UPDATE cuentas SET saldo = saldo + 45000 WHERE nombre = 'Lider';
    COMMIT;
ELSE
    ROLLBACK;
END IF;
