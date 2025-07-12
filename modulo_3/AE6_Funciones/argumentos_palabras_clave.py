# Ejemplo de uso de argumentos con palabras clave

def saludar(nombre="Estudiante", ciudad="Chile"):
    print(f"Hola {nombre}, ¿cómo está el clima en {ciudad}?")

saludar()  # Usa valores por defecto
saludar("Cristian", "Temuco")
saludar(nombre="María", ciudad="Valdivia")
saludar(ciudad="Iquique", nombre="Luis")
