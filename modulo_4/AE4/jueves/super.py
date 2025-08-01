class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Gato(Animal):
    def __init__(self, nombre, tipo_pelaje):
        super().__init__(nombre)
        self.tipo_pelaje = tipo_pelaje