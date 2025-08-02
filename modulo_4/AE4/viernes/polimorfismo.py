class MedioDePago:
    def pagar(self):
        raise NotImplementedError("Debes implementar este método en la subclase.")

class RedCompra(MedioDePago):
    def pagar(self):
        print("Pagando con RedCompra...")

class WebPay(MedioDePago):
    def pagar(self):
        print("Pagando con WebPay desde el navegador...")

class Cheque(MedioDePago):
    def pagar(self):
        print("Pagando con cheque, esperar confirmación bancaria.")

# Lista de medios de pago
pagos = [RedCompra(), WebPay(), Cheque()]

for metodo in pagos:
    metodo.pagar()

""" Este es un ejemplo claro de polimorfismo: 
mismo método pagar() → diferentes respuestas.

raise NotImplementedError obliga a las clases 
hijas a implementar el método."""