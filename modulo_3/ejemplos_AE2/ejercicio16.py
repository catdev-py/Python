# === EJERCICIO 16: Scope (Alcance de Variables)
#Global: Se ve en todo el programa.
#Local: Solo dentro de funciones.
print("\n--- EJERCICIO 16 ---")
saludo = "Hola"

def saludar():
    nombre = "Matías"
    print(saludo, nombre)  # Puede usar 'saludo' global y 'nombre' local

saludar()
#print(nombre)  # ERROR, 'nombre' solo existe dentro de la función