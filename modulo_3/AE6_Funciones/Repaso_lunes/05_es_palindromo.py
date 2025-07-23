# Ejercicio 5: Verificar si una palabra es un palíndromo

palabra = input("Ingrese una palabra: ").lower()
if palabra == palabra[::-1]:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")