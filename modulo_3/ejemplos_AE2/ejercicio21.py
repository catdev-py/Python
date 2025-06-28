# === EJERCICIO 21: break y continue
print("\n--- EJERCICIO 21 ---")
for numero in range(5):
    if numero == 3:
        break  # Sale del ciclo
    print(numero)

for numero in range(5):
    if numero == 2:
        continue  # Salta esta vuelta
    print(numero)