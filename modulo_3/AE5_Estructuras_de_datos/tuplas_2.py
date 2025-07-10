
# MINI-TALLER: Tuplas en Python - Nivel básico
# Objetivo: Crear y consultar tuplas

# Crear una tupla con vocales
vocales = ("a", "e", "i", "o", "u")
suma = sum(vocales)
print("Suma de vocales:", suma)

print("Tupla de vocales:", vocales)

# Acceder a un valor de la tupla por su índice
print("Primera vocal:", vocales[0])

# Intentar modificar la tupla generará error
# vocales[0] = "A"  # ← Esto generará un TypeError

# Las tuplas pueden tener distintos tipos de datos
gato = ("Miu", 5, "persa", False)
print("Nombre del gato:", gato[0])

# Agregar un valor (realmente crea una nueva tupla)
gato = gato + ("4.1",)
print("Tupla extendida:", gato)

# ACTIVIDAD:
# Crea una tupla con los datos de tu comida favorita:
# nombre (str), tipo (str), precio (int), vegetariano (bool)

comida = ("lasagna", "plato italiano", 2000, True)

comida2 = ("fideos con salsa","plato italiano",1500,False)
