# archivo: persona.py
class Persona:
    """Define una persona con nombre y edad."""

    def __init__(self, nombre, edad): #define el constructor.
        
        self.nombre = nombre    # crea el atributo nombre.
        self.edad = edad        # crea el atributo edad.d

    def saludar(self): # método que utiliza los atributos para imprimir un saludo
        
        print(f"¡Hola! Soy {self.nombre} y tengo {self.edad} años.")


