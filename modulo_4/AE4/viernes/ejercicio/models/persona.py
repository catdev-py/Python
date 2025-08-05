from models.chinimal import Chinimal

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.chinimales = []

    def adoptar_chinimal(self, chinimal: Chinimal):
        self.chinimales.append(chinimal)
        print(f"{self.nombre} adoptó a {chinimal.nombre} 🐾")

    def alimentar_chinimal(self, chinimal: Chinimal, alimento):
        print(f"{self.nombre} alimenta a {chinimal.nombre} con {alimento}.")
        chinimal.alimentar(alimento)

    def hacer_actividad_con_chinimal(self, chinimal: Chinimal):
        print(f"{self.nombre} realiza actividad saludable con {chinimal.nombre}.")
        chinimal.hacer_actividad(chinimal.actividad_saludable)
