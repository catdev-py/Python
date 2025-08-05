from models.chinimal import Chinimal
from settings import DURACION_DIA
import time

chinimales = []
duracion_dia = 10  # duración por defecto en segundos

def crear_chinimal():
    nombre = input("Nombre del Chinimal: ")
    especie = input("Especie: ")
    color = input("Color: ")
    comida = input("¿Qué comida saludable debe consumir? ")
    actividad = input("¿Qué actividad saludable debe hacer? ")
    chinimal = Chinimal(nombre, especie, color, comida, actividad)
    chinimales.append(chinimal)
    print(f"✅ Se ha creado a {nombre} el {especie}.\n")

def alimentar_chinimal():
    mostrar_chinimales()
    idx = int(input("¿Cuál Chinimal quieres alimentar? [número] ")) - 1
    comida = input("¿Qué comida le das? ")
    chinimales[idx].alimentar(comida)

def actividad_chinimal():
    mostrar_chinimales()
    idx = int(input("¿Con cuál Chinimal quieres hacer actividad? [número] ")) - 1
    actividad = input("¿Qué actividad realizará? ")
    chinimales[idx].hacer_actividad(actividad)

def pasar_dia():
    print("⏳ Pasando un día...")
    time.sleep(duracion_dia)
    for chinimal in chinimales:
        chinimal.pasar_dia()

def mostrar_chinimales():
    print("\nChinimales disponibles:")
    for i, ch in enumerate(chinimales):
        print(f"{i+1}. {ch.nombre} ({ch.especie})")

def configurar_duracion_dia():
    global duracion_dia
    duracion_dia = int(input("Ingrese duración de un día (en segundos): "))
    print(f"✅ Duración de día actualizada a {duracion_dia} segundos.\n")

def menu():
    while True:
        print("\n🐾 MENÚ PRINCIPAL")
        print("1. Crear nuevo Chinimal")
        print("2. Alimentar Chinimal")
        print("3. Realizar actividad con Chinimal")
        print("4. Pasar un día")
        print("5. Configurar duración del día")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_chinimal()
        elif opcion == "2":
            alimentar_chinimal()
        elif opcion == "3":
            actividad_chinimal()
        elif opcion == "4":
            pasar_dia()
        elif opcion == "5":
            configurar_duracion_dia()
        elif opcion == "6":
            print("¡Hasta luego! 🖐️")
            break
        else:
            print("Opción inválida.")
