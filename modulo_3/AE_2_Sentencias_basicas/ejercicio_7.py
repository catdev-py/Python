""" 
Creación y Manipulación de Objetos - Como armar tu propio personaje
Los objetos son como personajes o cosas, con sus datos (atributos) y acciones (métodos). 
"""
# Definimos la clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear un objeto
persona1 = Persona("Marcelo", 30)

# Acceder a sus atributos
print(persona1.nombre)
print(persona1.edad)

# Modificar atributos
persona1.edad = 31
print(persona1.edad)

# Agregar atributo dinámico
persona1.ciudad = "Santiago"
print(persona1.ciudad)

# Eliminar un atributo
del persona1.ciudad
# print(persona1.ciudad)  # Esto da error porque ya no existe
