""" 
Desafío Extra:
Simula un sistema para decidir 
si se suspenden las clases por mal tiempo en el sur: 
"""
temperatura = int(input("Ingrese la temperatura actual: "))
nevando = input("¿Está nevando? (sí/no): ")

if temperatura < 0 and nevando == "sí":
    print("Se suspenden las clases por mal tiempo")  
else:
    print("Clases normales")  
