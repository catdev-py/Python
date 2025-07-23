# Ejercicio 10: Contar vocales en una frase

frase = input("Ingrese una frase: ").lower()
vocales = 'aeiou'
conteo = {v: frase.count(v) for v in vocales}
print("Cantidad de vocales:", conteo)