""" 
Operadores Lógicos - Verdadero o Falso
Los operadores lógicos sirven para tomar decisiones combinando condiciones.

Operador	Significado
and	Verdadero si ambas son verdaderas
or	Verdadero si al menos una es verdadera
not	Invierte el resultado (True → False y viceversa) 
"""
# Edad para entrar a una fiesta
edad = 20
tiene_entrada = True

# Puede entrar si tiene entrada y es mayor de 18
puede_entrar = edad > 18 and tiene_entrada
print("¿Puede entrar?", puede_entrar)

# No puede entrar si no tiene entrada
tiene_entrada = False
puede_entrar = edad > 18 and tiene_entrada
print("¿Puede entrar?", puede_entrar)

# Usando not
print("¿No tiene entrada?", not tiene_entrada)
