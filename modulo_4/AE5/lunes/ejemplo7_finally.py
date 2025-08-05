try:
    archivo = open("ventas.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("Archivo no encontrado.")
finally:
    print("Cerrando archivo (aunque no exista).")
    try:
        archivo.close()
    except NameError:
        print("No se abrió ningún archivo.")