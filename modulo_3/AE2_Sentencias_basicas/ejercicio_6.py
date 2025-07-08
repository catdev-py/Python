# break y continue - Controlando el ciclo
# Romper el ciclo con break
for numero in range(10):
    if numero == 5:
        print("Se detiene en", numero)
        break
    print(numero)

# Saltar una vuelta con continue
for numero in range(5):
    if numero == 2:
        print("Saltamos el 2")
        continue
    print(numero)
