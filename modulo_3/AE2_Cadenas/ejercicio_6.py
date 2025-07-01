""" 
Métodos útiles de Cadenas
Las cadenas tienen poderes especiales, llamados métodos, 
que nos ayudan a trabajar con textos. Aquí te muestro ejemplos: 
"""
mensaje = "Hola, Bienvenidos al Bootcamp de Python"

m = ("Hola, Bienvenidos al Bootcamp de Python").upper()
print(m)

# Poner todo en mayúsculas
print(mensaje.upper())

# Poner todo en minúsculas
print(mensaje.lower())

# Contar cuántas veces aparece una letra
print(mensaje.count("o"))

# Dividir el texto en palabras
print(mensaje.split(" "))

# Encontrar la posición de una palabra
print(mensaje.find("Bootcamp"))

# Revisar si es alfanumérico (sin espacios ni símbolos)
solo_letras = "Python3"
print(solo_letras.isalnum())

# Revisar si termina en cierta palabra
print(mensaje.endswith("Python"))
