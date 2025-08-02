class Animal:
    def hacer_sonido(self):
        raise NotImplementedError

class Perro(Animal):
    def hacer_sonido(self):
        print("woof woof")

class Gato(Animal):
    def hacer_sonido(self):
        print("miiiaaaaauuu")
        
animales = [Perro(), Gato()]

for animal in animales:
    animal.hacer_sonido()