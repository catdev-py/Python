# Conversión de Tipos (Type Casting)
""" 
Podemos convertir:
De número a texto → str()
De texto a número → int() (solo si el texto es un número válido) 
"""
tiempo_preparacion = 1
tiempo_horneado = "2"

# Si sumamos directo, da error
# tiempo_total = tiempo_preparacion + tiempo_horneado  # ERROR

# Convertimos el texto a número
tiempo_total = tiempo_preparacion + int(tiempo_horneado)
print("Tiempo total:", tiempo_total, "horas")
