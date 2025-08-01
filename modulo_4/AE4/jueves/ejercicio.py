class Vehiculo:
    def arrancar(self):
        print("Arranca...")

class Auto(Vehiculo):
    def arrancar(self):
        print("Auto encendido")

class Bicicleta(Vehiculo):
    def arrancar(self):
        print("Pedaleando")