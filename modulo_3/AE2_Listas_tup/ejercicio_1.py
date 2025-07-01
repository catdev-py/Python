""" 
Listas - La Mochila de Python
Las listas son como una mochila donde guardas cosas en un orden y 
puedes sacar o poner más cosas cuando quieras. 
"""
# Crear una lista
mochila = ["Cuaderno", "Lápiz", "Botella de agua"]

print(mochila)  # Muestra toda la mochila

# Operaciones comunes:
# Agregar al final
mochila.append("Sandwich")
print(mochila)

# Insertar en una posición específica (posición 1)
mochila.insert(1, "Cargador")
print(mochila)

# Eliminar un elemento por su valor
mochila.remove("Lápiz")
print(mochila)

# Eliminar el último elemento
mochila.pop()
print(mochila)

# Eliminar un elemento por su posición
mochila.pop(0)
print(mochila)
