# Métodos de listas
# Lista de nombres
nombres = ["Juan", "Pedro", "María", "Lucía"]

print("Lista original:", nombres)

# Agregar un nuevo nombre al final
nombres.append("Sofía")
print("Después de agregar Sofía:", nombres)

# Eliminar al último de la lista
nombres.pop()
print("Después de eliminar el último:", nombres)

# Invertir el orden
nombres.reverse()
print("Lista invertida:", nombres)

# Ordenar alfabéticamente
nombres.sort()
print("Lista ordenada:", nombres)

# Buscar la posición de un elemento
posicion = nombres.index("María")
print("Posición de María en la lista:", posicion)
