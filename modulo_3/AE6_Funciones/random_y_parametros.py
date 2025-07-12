# Ejemplo usando el módulo random y parámetros por defecto

import random

def lanzar_dados(cantidad=1, caras=6):
    for i in range(cantidad):
        print("Dado", i+1, "->", random.randint(1, caras))

lanzar_dados()                # Lanza 1 dado de 6 caras
lanzar_dados(3)               # Lanza 3 dados de 6 caras
lanzar_dados(cantidad=2, caras=10)  # Lanza 2 dados de 10 caras
