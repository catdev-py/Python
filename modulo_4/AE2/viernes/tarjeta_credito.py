class TarjetaCredito:
    def __init__(self, saldo_pagar, limite_credito, tasa_interes):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.tasa_interes = tasa_interes

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
            print("Compra realizada.")
        else:
            print("Límite excedido.")

    def resumen(self):
        return f"Saldo: ${self.saldo_pagar}"
