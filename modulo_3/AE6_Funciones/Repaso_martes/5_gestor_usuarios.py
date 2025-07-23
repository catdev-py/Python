# Gestión básica de usuarios usando diccionarios y condicionales

usuarios = {}

def registrar_usuario():
    usuario = input("Nombre de usuario: ")
    email = input("Correo electrónico: ")
    if usuario in usuarios:
        print("Ese usuario ya está registrado.")
    else:
        usuarios[usuario] = email
        print(f"Usuario {usuario} registrado correctamente.")

def ver_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for nombre, correo in usuarios.items():
            print(f"{nombre} -> {correo}")

while True:
    print("\nGestor de Usuarios")
    print("1. Registrar nuevo usuario")
    print("2. Ver usuarios registrados")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        ver_usuarios()
    elif opcion == "3":
        break
    else:
        print("Opción inválida.")