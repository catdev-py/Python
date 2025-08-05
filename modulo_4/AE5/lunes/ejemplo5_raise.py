def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

try:
    print(dividir(10, 2))
    print(dividir(10, 0))
except ZeroDivisionError as e:
    print(f"Error capturado: {e}")