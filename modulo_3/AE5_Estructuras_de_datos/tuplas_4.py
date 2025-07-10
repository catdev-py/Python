# Tupla original
gato = ('Miu', 5, 'persa', False)
print("Original:", gato)

# Intento de modificar un valor (esto sí lanza error)
try:
    gato[0] = "GatoModificado"
except TypeError as e:
    print("Error al intentar modificar la tupla:", e)

# Ahora unimos la tupla original con una nueva
gato = gato + ("4.1",)

# Ahora gato apunta a una nueva tupla
print("Nueva tupla:", gato)
