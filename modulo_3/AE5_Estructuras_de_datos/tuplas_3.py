# Ejemplo de tupla sin paréntesis

# En Python, una tupla también puede definirse sin paréntesis, separando los elementos por comas
colores = "rojo", "verde", "azul"
print("tupla sin paréntesis:", colores)

# Mostramos el tipo de variable para confirmar que es una tupla
print("Tipo de 'colores':", type(colores))

# Mostramos los elementos de la tupla
print("Tupla completa:", colores)

# Accedemos a un elemento de la tupla
print("Primer color:", colores[0])
print("Tercer color:", colores[2])

# Intentamos modificar un elemento (esto dará error porque las tuplas son inmutables)

try:
    colores[0] = "amarillo"
except TypeError as e:
    print("Error al intentar modificar la tupla:", e)
