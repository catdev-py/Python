class TarjetaCredito:
    
    def __init__(self, limite_credito, saldo_pagar):
        self.limite_credito = limite_credito  # Límite máximo permitido
        self.saldo_pagar = saldo_pagar        # Lo que ya ha usado el usuario

    def hacer_compra(self, monto):  # Recibe el monto de la compra
        if TarjetaCredito.puede_comprar(self.limite_credito, self.saldo_pagar, monto):
            self.saldo_pagar += monto  # Aumenta el saldo a pagar
            print(f"Compra aprobada por ${monto}. Saldo a pagar: ${self.saldo_pagar}")
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self

    @staticmethod
    def puede_comprar(limite, saldo_utilizado, monto):
        return (saldo_utilizado + monto) <= limite
       
c1 = TarjetaCredito(1000, 0)
c1.hacer_compra(500)   # Compra aprobada

c2 = TarjetaCredito(1000, 0)
c2.hacer_compra(1000)  # Compra aprobada

c3 = TarjetaCredito(1000, 0)
c3.hacer_compra(2000)  # Tarjeta Rechazada