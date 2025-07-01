""" 
Interpolación de Cadenas
Forma moderna: Usando f-strings 
"""
nombre = "Marcelo"
edad = 29
altura = 1.75

print(f"Mi nombre es {nombre} y tengo {edad} años")

# Forma clásica: Usando .format()
print("Mi nombre es {} y tengo {} años".format(nombre, edad))

# El orden importa:
print("Tengo {} años y me llamo {}".format(edad, nombre))

# Forma antigua: Usando %
print("Me llamo %s y tengo %d años y mido %.2f metros" % (nombre, edad, altura))
# %s → texto
# %d → número entero
# %.2f → número con dos decimales