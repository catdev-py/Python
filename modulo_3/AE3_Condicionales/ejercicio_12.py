while True:
    edad_input = input("Ingrese su edad (entre 1 y 102): ")

    if edad_input.isdigit():  # Verifica que sea un número entero positivo
        edad = int(edad_input)

        if 1 <= edad <= 102:
            break  # Edad válida, salimos del bucle
        else:
            print("Por favor, ingrese una edad real entre 1 y 102 años.")
    else:
        print("Por favor, ingrese solo números enteros.")

# Lógica de votación
if edad < 18:
    print("No puedes votar 😢")
elif edad <= 60:
    print("Votación obligatoria 🗳️")
else:
    print("Puedes votar, pero es voluntario 👴🏻👵🏻")