class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Creando Animal llamado {self.nombre}")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llama al constructor de Animal
        self.raza = raza
        print(f"Es un perro de raza {self.raza}")

mi_perro = Perro("Firulais", "Labrador")

# Salida:
# Creando Animal llamado Firulais
# Es un perro de raza Labrador