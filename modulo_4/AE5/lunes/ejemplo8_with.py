try:
    with open("ventas.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("Archivo no encontrado.")