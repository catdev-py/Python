""" 
Concatenar Cadenas y Variables
Concatenar significa unir o juntar varias partes de texto o variables.
"""
# Forma 1: Usando comas en print 
nombre = "Marcelo"
print("Me llamo", nombre)
# Ventaja: Agrega un espacio automático entre las palabras.

# Forma 2: Usando el símbolo +
nombre = "Marcelo"
print("Mi nombre es " + nombre)

# Ojo: Si no ponemos espacios dentro de las comillas, las palabras quedan pegadas.
apellido = "González"
print("Mi nombre es " + nombre + apellido)  # ¡Quedan pegadas!
print("Mi nombre es " + nombre + " " + apellido)  # Así queda bien
