class TarjetaCredito:
    # Atributos de clase
    banco = "Banco Internacional de Programadores"
    todas_las_tarjetas = []

    def __init__(self, limite_credito, saldo_pagar):
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar
        TarjetaCredito.todas_las_tarjetas.append(self)

    @classmethod
    def cambiar_banco(cls, nombre):
        cls.banco = nombre

    @classmethod
    def todos_saldos(cls):
        total_saldos = 0
        for tarjeta in cls.todas_las_tarjetas:
            total_saldos += tarjeta.saldo_pagar
        return total_saldos

# Crear tarjetas con distintos saldos
t1 = TarjetaCredito(1000, 200)
t2 = TarjetaCredito(1500, 500)
t3 = TarjetaCredito(2000, 1000)

# Mostrar banco actual
print(f"Banco actual: {TarjetaCredito.banco}")

# Cambiar banco
TarjetaCredito.cambiar_banco("Banco Python Financiero")
print(f"Nuevo banco: {TarjetaCredito.banco}")

# Mostrar el saldo de cada tarjeta
print(f"Saldo tarjeta 1: {t1.saldo_pagar}")
print(f"Saldo tarjeta 2: {t2.saldo_pagar}")
print(f"Saldo tarjeta 3: {t3.saldo_pagar}")

# Mostrar el total de saldos a pagar de todas las tarjetas
print(f"Total de saldos a pagar: {TarjetaCredito.todos_saldos()}")
