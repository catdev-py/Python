# Agenda personal tipo To-Do list

agenda = []

def mostrar_agenda():
    if not agenda:
        print("La agenda está vacía.")
    else:
        for i, tarea in enumerate(agenda, start=1):
            print(f"{i}. {tarea}")

def agregar_tarea():
    tarea = input("Ingrese una nueva tarea: ")
    agenda.append(tarea)
    print("Tarea agregada.")

def eliminar_tarea():
    mostrar_agenda()
    try:
        indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(agenda):
            eliminada = agenda.pop(indice)
            print(f"Tarea '{eliminada}' eliminada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, ingrese un número.")

while True:
    print("\nAgenda Personal")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_agenda()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        break
    else:
        print("Opción inválida.")