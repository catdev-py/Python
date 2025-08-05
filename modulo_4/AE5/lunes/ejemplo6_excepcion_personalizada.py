class SaldoInsuficiente(Exception):
    pass

def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficiente("Saldo insuficiente para retirar.")
    return saldo - monto

try:
    saldo = 5000
    print(f"Saldo inicial: {saldo}")
    saldo = retirar(saldo, 10000)
except SaldoInsuficiente as e:
    print(f"Error capturado: {e}")