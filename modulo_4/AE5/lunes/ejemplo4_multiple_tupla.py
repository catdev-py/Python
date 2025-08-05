try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except (ValueError, ZeroDivisionError):
    print("Ocurrió un error en la entrada.")
    