""" 
Sentencias Condicionales - Elige un camino
Como en un videojuego: si se cumple algo, haces una cosa; si no, haces otra. 
"""
edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Eres mayor de edad, puedes votar.")
elif edad >= 16:
    print("Eres casi mayor, pero aún no puedes votar.")
else:
    print("Eres menor de edad.")

# Combinando condiciones:
nota = 7
asistencia = 85

if nota >= 6 and asistencia >= 80:
    print("Aprobaste la materia.")
else:
    print("Debes mejorar.")
