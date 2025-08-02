class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_truco(self):
        print(f"{self.nombre} hace un truco")

class Gato(Animal):
    def hacer_truco(self):
        print(f"{self.nombre} te ignora")
        print(f"{self.nombre} se rehúsa a hacer el truco")

miau = Gato("Miau")
miau.hacer_truco()