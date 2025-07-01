# === EJERCICIO 23: Ejercicio Final
print("\n--- EJERCICIO 23 ---")
productos = {
    "completo": 2500,
    "empanada": 1500,
    "bebida": 1000
}

carrito = []
total = 0

carrito.append("completo")
carrito.append("bebida")

for producto in carrito:
    total += productos[producto]

print(f"Total a pagar: ${total}")

# total = total + productos[producto]
# total += productos[producto] Forma abreviada

#Cálculo del total
# total = 0

# for producto in carrito:
#    total += productos[producto]
# Primera vuelta:
# producto = "completo"
# total += productos["completo"] → total += 2500 → total = 2500

# Segunda vuelta:
# producto = "bebida"
# total += productos["bebida"] → total += 1000 → total = 3500