# Simulador de biblioteca - gestión básica

biblioteca = {}

def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor: ")
    anio = input("Ingrese el año de publicación: ")
    biblioteca[titulo] = {"autor": autor, "año": anio}
    print(f"Libro '{titulo}' agregado.")

def buscar_libro():
    titulo = input("Ingrese el título a buscar: ")
    if titulo in biblioteca:
        print("Libro encontrado:", biblioteca[titulo])
    else:
        print("Libro no encontrado.")

def listar_libros():
    if not biblioteca:
        print("No hay libros en la biblioteca.")
    else:
        for titulo, info in biblioteca.items():
            print(f"{titulo} - {info['autor']} ({info['año']})")

while True:
    print("\nGestor Biblioteca - Menú")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Listar libros")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        buscar_libro()
    elif opcion == "3":
        listar_libros()
    elif opcion == "4":
        print("Saliendo del gestor.")
        break
    else:
        print("Opción inválida.")