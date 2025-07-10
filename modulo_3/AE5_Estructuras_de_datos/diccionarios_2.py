
# MINI-TALLER: Diccionarios en Python - Nivel básico
# Objetivo: Crear, modificar y consultar diccionarios

# Crear un diccionario de estudiante
estudiante = {"nombre": "Gonzalo", "curso": "Python"}
print("Estudiante:", estudiante)

# Acceder al valor de una clave
print("Nombre del estudiante:", estudiante["nombre"])

# Modificar el valor de una clave
estudiante["nombre"] = "Vicente"
print("Nombre actualizado:", estudiante["nombre"])

# Verificar existencia de una clave
if "curso" in estudiante:
    print("El curso es:", estudiante["curso"])

# ACTIVIDAD:
# Crea un diccionario con los datos de una mascota (nombre, especie, edad, vacunado)

# Cecilia
# mascota = {"nombre" : "Mimi", "especie" : "perruna", "edad" : 8, "vacunado" : True}

# Cristian
""" mascota = {
    "nombre": "Charles Mariano",
    "especie": "Perro",
    "edad": 5,
    "vacunado": True
} """

# Catalina
""" Mascota = {
    "nombre": "Mushu",
    "especie": "felino",
    "edad": 6,
    "vacunado": True
} """

# ALicia
""" mi_gato = {
    "nombre": "Compadre Moncho",
    "especie": "gato doméstico de pelo largo",
    "edad": 20,
    "vacunado": True
}
for i in mi_gato.items():
    print(i) """

# Crear un diccionario con los datos de un videojuego
# nombre, plataforma, género, tipo, precio, personajes, lo estás jugando? 
# recorrer el diccionario e imprimir las claves, los valores y los items

# Nathalia
""" print("\n--- Nathalia ---")
game = {
    "nombre": "Mario",
    "plataforma": "Nintendo",
    "genero": "Aventura",
    "precio": 59.99,
    "personajes" : ["Mario", "Luigi", "Peach"],
    "multijugador": True,
    "Lo estás jugando?": True,
}
for i in game.items():
    print(i) """
  
# Cecilia
""" print("\n--- Cecilia ---")  
videojuego = {"nombre" : "Age of Empires", "plataforma" : "PC", "genero" : "Estrategia", "tipo" : "???", "precio" : 20990, "personajes" : "nn", "lo estás jugando?" : False}
for i in videojuego.items():
    print(i) """
    
# Darío
""" print("\n--- Darío ---")
videojuego = {
"nombre" : "Silent Hill 2 Remake",
"plataforma" : "PC", 
"género" : "Terror psicológico", 
"tipo" : "Exploración", 
"precio" : 60, 
"personajes" : ["James Sunderland, Angela Orosco, Maria"], 
"lo estás jugando?" : True, 
}
for i in videojuego.items():
    print(i) """
    
# Cristian
print("\n--- Cristian ---")  
juego = {
    "nombre": "Sekiro: Shadows Die Twice",
    "plataforma": "PC",
    "genero": "Aventura",
    "tipo": "Souls-like",
    "precio": 47650,
    "personajes": ["Sekiro", "Isshin Ashina", "Genichiro Ashina"],
    "jugando": False
}
for i in juego.items():
    print(i)
for i in juego.keys():
    print(f"Clave: {i}")
for i in juego.values():
    print(f"Valor: {i}")