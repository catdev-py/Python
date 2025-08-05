import time
from settings import DURACION_DIA

class Chinimal:
    def __init__(self, nombre, especie, color, comida_saludable, actividad_saludable, salud=100, felicidad=100, energia=100):
        self.nombre = nombre
        self.especie = especie
        self.color = color
        self.comida_saludable = comida_saludable
        self.actividad_saludable = actividad_saludable
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia
        self.dias_sin_comer = 0
        self.dias_sin_actividad = 0

    def alimentar(self, comida):
        if comida.lower() == self.comida_saludable.lower():
            self.salud += 15
            self.felicidad += 10
            self.dias_sin_comer = 0
            print(f"{self.nombre} comió su comida favorita: {comida} 🍽️")
        else:
            self.salud -= 5
            self.felicidad -= 5
            print(f"A {self.nombre} no le gustó esa comida. 😟")

        self.mostrar_estado()

    def hacer_actividad(self, actividad):
        if actividad.lower() == self.actividad_saludable.lower():
            self.felicidad += 15
            self.energia += 10
            self.dias_sin_actividad = 0
            print(f"{self.nombre} hizo su actividad favorita: {actividad} 🐾")
        else:
            self.felicidad -= 5
            self.energia -= 5
            print(f"{self.nombre} no disfruta esa actividad. 😒")

        self.mostrar_estado()

    def pasar_dia(self):
        self.dias_sin_comer += 1
        self.dias_sin_actividad += 1

        if self.dias_sin_comer >= 2:
            self.salud -= 10
            print(f"{self.nombre} está debilitado por no comer. 🥺")

        if self.dias_sin_actividad >= 2:
            self.felicidad -= 10
            print(f"{self.nombre} está triste por no hacer lo que le gusta. 😞")

        self.energia -= 5
        self.mostrar_estado()

    def mostrar_estado(self):
        def emoticones(valor):
            if valor >= 80: return "😄"
            elif valor >= 50: return "😐"
            else: return "😢"

        print(f"🐾 Estado de {self.nombre} ({self.especie}):")
        print(f"   Salud: {self.salud} {emoticones(self.salud)}")
        print(f"   Felicidad: {self.felicidad} {emoticones(self.felicidad)}")
        print(f"   Energía: {self.energia} {emoticones(self.energia)}\n")
