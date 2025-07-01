"""
Booleanos - Respuestas Verdadero o Falso
Los booleanos son respuestas tipo:
True = Verdadero
False = Falso
"""
# Ejemplo de comparación
mayor_edad = 20 > 18
print(mayor_edad)  # True

# Operadores lógicos
llueve = True
hay_paraguas = True

# Quiero salir si no llueve o si tengo paraguas
salgo = not llueve or hay_paraguas
print(salgo)  # False

# True and True = True
# True and False = False
# False or True = True
# False or False = False

#  4 != 2 
# 4 > 2

if (4 != 2) and (4 > 2):
    print("Verdadero")
else:
    print("Falso")