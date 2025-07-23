# Simulador de reservas de tickets para conciertos

eventos = {
    "Rock": 10,
    "Jazz": 5,
    "Clásica": 8
}

def mostrar_eventos():
    for evento, cupos in eventos.items():
        print(f"{evento}: {cupos} tickets disponibles")

def reservar_ticket():
    mostrar_eventos()
    eleccion = input("¿Qué concierto desea reservar? ").capitalize()
    if eleccion in eventos and eventos[eleccion] > 0:
        eventos[eleccion] -= 1
        print(f"Reserva confirmada para {eleccion}.")
    else:
        print("Evento no disponible o sin cupos.")

while True:
    print("\nSistema de Reserva de Tickets")
    print("1. Ver eventos")
    print("2. Reservar ticket")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_eventos()
    elif opcion == "2":
        reservar_ticket()
    elif opcion == "3":
        print("Gracias por usar el sistema.")
        break
    else:
        print("Opción inválida.")