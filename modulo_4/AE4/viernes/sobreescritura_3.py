# Clase base
class Vehiculo:
    def avanzar(self):
        print("El vehículo avanza...")

# Clase hija: Micro del Transantiago
class Micro(Vehiculo):
    def avanzar(self):
        print("La micro avanza con paradas cada 3 cuadras.")

# Clase hija: Metro
class Metro(Vehiculo):
    def avanzar(self):
        print("El metro avanza sin detenerse entre estaciones.")

# Probamos
transporte_1 = Micro()
transporte_2 = Metro()

transporte_1.avanzar()
transporte_2.avanzar()

""" Se usa el mismo método avanzar() en ambas clases, 
pero se comportan diferente.

Este ejemplo muestra sobreescritura: la clase hija 
reemplaza el comportamiento del padre."""