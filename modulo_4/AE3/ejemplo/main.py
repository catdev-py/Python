from datetime import datetime
from models import Admin, Usuario, Boleto, Pelicula, Funcion

# Simulación de autenticación básica
ADMIN_PASSWORD = "admin123"
USER_PASSWORD = "user123"

# Instanciamos los objetos
admin = Admin("Administrador", "admin@example.com", "admin123")
usuario = Usuario("Usuario", "usuario@example.com", "user123")


def ingresar():
    contraseña = input("Ingrese su contraseña: ")
    if contraseña == ADMIN_PASSWORD:
        print("Bienvenido, Administrador.")
        menu_admin()
    elif contraseña == USER_PASSWORD:
        print("Bienvenido, Usuario.")
        menu_usuario()
    else:
        print("Contraseña incorrecta.")

def menu_usuario():
    while True:
        print("\nMenú Usuario")
        print("1. Consultar Horarios")
        print("2. Comprar Boleto")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Funcion.consultar_horarios()
        elif opcion == "2":
            seleccionar_funcion_y_comprar()
        elif opcion == "3":
            print("Sesión cerrada.")
            break
        else:
            print("Opción inválida.")

def menu_admin():
    while True:
        print("\nMenú Administrador")
        print("1. Consultar Horarios")
        print("2. Comprar Boleto")
        print("3. Agregar Película")
        print("4. Agregar Función")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Funcion.consultar_horarios()
        elif opcion == "2":
            seleccionar_funcion_y_comprar()
        elif opcion == "3":
            admin.agregar_pelicula()
        elif opcion == "4":
            admin.agregar_funcion()
        elif opcion == "5":
            print("Sesión de administrador cerrada.")
            break
        else:
            print("Opción inválida.")

# ✅ Esta función es auxiliar y solo selecciona la función y la cantidad.
# ✅ La lógica de comprar está en usuario.comprar_boleto(...)
def seleccionar_funcion_y_comprar():
    funciones = Funcion.funciones
    if not funciones:
        print("No hay funciones disponibles para comprar boletos.")
        return

    print("\nSeleccione una función:")
    for i, funcion in enumerate(funciones, 1):
        print(f"{i}. {funcion}")

    seleccion = input("Ingrese el número de la función: ")
    if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(funciones)):
        print("Selección inválida.")
        return

    funcion_seleccionada = funciones[int(seleccion) - 1]

    cantidad_input = input("¿Cuántos boletos desea comprar?: ")
    if not cantidad_input.isdigit() or int(cantidad_input) <= 0:
        print("Cantidad inválida.")
        return

    cantidad = int(cantidad_input)

    # ✅ Aquí se llama al método correcto
    usuario.comprar_boleto(funcion_seleccionada, cantidad)

def main():
    while True:
        print("\n🎬 CineClub - Menú Principal")
        print("1. Ingresar")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar()
        elif opcion == "2":
            print("Gracias por usar CineClub. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
