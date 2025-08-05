class SaldoInsuficiente(Exception):
    pass

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        self._registrar(f"Depósito: ${monto}")
        print(f"Depósito exitoso. Saldo actual: ${self.saldo}")

    def retirar(self, monto):
        if monto > self.saldo:
            raise SaldoInsuficiente("Saldo insuficiente para retirar.")
        self.saldo -= monto
        self._registrar(f"Retiro: ${monto}")
        print(f"Retiro exitoso. Saldo actual: ${self.saldo}")

    def _registrar(self, movimiento):
        with open("movimientos.txt", "a") as archivo:
            archivo.write(f"{self.titular} - {movimiento}\n")

cuenta = CuentaBancaria("Cristian", 5000)
cuenta.depositar(2000)
try:
    cuenta.retirar(10000)
except SaldoInsuficiente as e:
    print(f"Error: {e}")