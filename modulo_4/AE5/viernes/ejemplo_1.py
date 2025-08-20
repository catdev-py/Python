""" # Abrir un archivo para leer
file = open("mi_archivo.txt", "r")

# Leer todo el contenido del archivo
contenido = file.read()

print(contenido)

# Cerrar el archivo después de usarlo
file.close() """

""" # Leer todo el contenido
file = open("mi_archivo.txt", "r")
contenido = file.read()
print(contenido)
file.close()"""

""" # Leer una sola línea
file = open("mi_archivo.txt", "r")
linea = file.readline()
linea2 = file.readline()
print(linea+linea2)
file.close() """

"""# Escribir en un archivo
file = open("mi_archivo.txt", "w")
file.write("Esto es una nueva línea de texto.")
file.close()  """

"""# Añadir contenido a un archivo existente
file = open("mi_archivo.txt", "a")
file.write("nAñadiendo otra línea al final.")
file.close() """

""" with open("mi_archivo.txt", "r") as file:
    contenido = file.read()
    print(contenido) """
    
""" try:
    # Intentar abrir un archivo
    with open("mi_archivo.txt", "r") as file:
        contenido = file.read()
except FileNotFoundError:
    print("El archivo no existe.")
except IOError:
    print("Hubo un error al intentar leer el archivo.") """
    
""" # Leer un archivo binario
with open("empanada.jpg", "rb") as file:
    contenido_binario = file.read()
    print(contenido_binario[:10])  # Imprimir solo los primeros 10 bytes

# Escribir en un archivo binario
with open("empanada.jpg", "wb") as file:
    file.write(contenido_binario) """