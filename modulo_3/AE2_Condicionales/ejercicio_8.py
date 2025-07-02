""" 
Crea un programa que:
1. Pregunte la edad.
2. Si es menor de 18, imprima "No puedes votar".
3. Si tiene entre 18 y 60, imprima "Votación Obligatoria".
4. Si tiene más de 60, imprima "Puedes votar, pero es voluntario". 
"""
edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("No puedes votar 😢")
elif edad <= 60:
    print("Votación obligatoria 🗳️")
else:
    print("Puedes votar, pero es voluntario 👴🏻👵🏻")
