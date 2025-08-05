try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Debes ingresar un número válido.")
except ZeroDivisionError:
    print("No puedes dividir por cero.")