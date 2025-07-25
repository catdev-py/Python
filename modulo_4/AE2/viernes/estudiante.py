class Mochila:
    def __init__(self):
        self.utiles = []

    def agregar_util(self, item):
        self.utiles.append(item)

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mochila = Mochila()

    def guardar_util(self, item):
        self.mochila.agregar_util(item)

    def ver_mochila(self):
        print(f"{self.nombre} lleva: {self.mochila.utiles}")

nico = Estudiante("Nicolás")
nico.guardar_util("Cuaderno")
nico.ver_mochila()
