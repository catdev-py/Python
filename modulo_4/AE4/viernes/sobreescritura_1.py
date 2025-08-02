class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_truco(self):
        print(f"{self.nombre} da la pata")


class Gato(Animal):    
    def hacer_truco(self):  # Sobreescribe el método del padre
        super().hacer_truco()  # Llama primero al método de Animal
        print("Pero lo hace a regañadientes")


# Creamos un gato y le pedimos que haga un truco
michi = Gato("Michi")
michi.hacer_truco()
