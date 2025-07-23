# Ejercicio 4: Imprimir la tabla de multiplicar de un número

num = int(input("Ingrese un número: "))
print(f"Tabla del {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")