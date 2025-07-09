# Creando y manipulando Listas

# Creamos una lista con algunas frutas
frutas = ["manzana", "plátano", "naranja"]

# Mostramos toda la lista
print("Lista completa de frutas:", frutas)

# Mostramos solo la primera fruta (recuerda que la primera posición es 0)
print("Primera fruta:", frutas[0])

# Cambiamos un valor de la lista
frutas[1] = "kiwi"
print("Lista después de cambiar plátano por kiwi:", frutas)

# Agregamos una nueva fruta al final de la lista
frutas.append("sandía")
print("Lista después de agregar sandía:", frutas)

# Eliminamos la última fruta de la lista
frutas.pop()
print("Lista después de eliminar la última fruta:", frutas)

# Cuántas frutas hay en total
print("Cantidad total de frutas:", len(frutas))

# insertamos una fruta en la segunda posición
frutas.insert(1, "pera")
print("Lista con pera en la segunda posición:", frutas)

# consulta en clases (Johana)
pantalones = ["jeans", "buzo", "cotelle", "calza"]


cajonera = [pantalones, "camisetas", "calcetines"]
print(cajonera)

cajonera = [[{"pantalones": pantalones }], "camisetas", "calcetines"]
print(cajonera)
