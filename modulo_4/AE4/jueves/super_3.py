class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
            
    def hacer_truco(self):
        print(f"{self.nombre} da la pata")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
        
    def hacer_truco(self):
        super().hacer_truco()  # Llama al método del padre
        print(f"{self.nombre} también ladra")

mi_perro = Perro("Toby", "Beagle")
mi_perro.hacer_truco()

# Salida:
# Toby da la pata
# Toby tambien ladra