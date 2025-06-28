# === EJERCICIO 2: Manejo de errores ===
print("\n--- EJERCICIO 2 ---")
try: #try sirve para manejar errores
    resultado = 10 / 0
except ZeroDivisionError: #exception ejecuta este bloque
    print("No se puede dividir por cero")

#sin try
#resultado = 10 / 0
#print("Hola") #nunca se ejecuta

#resumen
#try 	Intenta ejecutar un código
#except 	Maneja el error si este ocurre