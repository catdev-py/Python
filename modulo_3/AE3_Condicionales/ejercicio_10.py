""" 
Desafío para la casa: Crear un programa 
que recomiende ropa según la temperatura 
"""
temp = int(input("¿Cuál es la temperatura en tu ciudad?: "))

if temp < 5:
    print("Parka y guantes, hace mucho frío")
elif temp < 15:
    print("Polerón o chaqueta ligera")
else:
    print("Con polera estás bien")
