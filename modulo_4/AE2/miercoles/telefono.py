class Telefono:
    def __init__(self, marca, modelo, color, numero):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.numero = numero

    def llamar(self, otro_numero):
        print(f"Llamando desde el número {self.numero} al número {otro_numero}...")


