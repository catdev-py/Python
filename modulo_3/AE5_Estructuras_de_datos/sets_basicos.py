# Sets para eliminar duplicados
# Los sets eliminan los valores duplicados automáticamente
numeros = {1, 2, 3, 2, 4, 3, 5}

print("Números sin duplicados:", numeros)

# Agregar un valor al set
numeros.add(6)
print("Después de agregar 6:", numeros)

# Intentar agregar un valor repetido
numeros.add(3)
print("Después de intentar agregar 3 otra vez:", numeros)
