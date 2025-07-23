# Ejercicio 9: Generar los primeros N términos de Fibonacci

n = int(input("Ingrese cuántos términos desea: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()