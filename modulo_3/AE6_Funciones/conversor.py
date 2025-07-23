# Conversor de dolar y euro a peso chileno
valor_usd = 957.23
valor_eur = 1110.81

#Menu
def menu():
    print("Bienvenido al conversor de monedas")
    print("1. Pesos Chilenos a Dolares")
    print("2. Pesos Chilenos a Euros")
    print("3. Dolares a Pesos Chilenos")
    print("4. Euros a Pesos Chilenos")
    print("5. Salir")
    
    opcion = int(input("Ingrese la opcion deseada: "))
    return opcion

def convertir_pesos_a_dolares(pesos):
    dolares = pesos / valor_usd
    return dolares

def convertir_pesos_a_euros(pesos): 
    euros = pesos / valor_eur
    return euros    

def convertir_dolares_a_pesos(dolares):
    pesos = dolares * valor_usd
    return pesos

def convertir_euros_a_pesos(euros): 
    pesos = euros * valor_eur
    return pesos

while True:
    opcion = menu()
    if opcion == 1:
        pesos = float(input("Ingrese la cantidad de pesos chilenos: "))
        dolares = convertir_pesos_a_dolares(pesos)
        print("El equivalente en dolares es:", dolares)
    elif opcion == 2:
        pesos = float(input("Ingrese la cantidad de pesos chilenos: "))
        euros = convertir_pesos_a_euros(pesos)
        print("El equivalente en euros es:", euros)
    elif opcion == 3:
        dolares = float(input("Ingrese la cantidad de dolares: "))
        pesos = convertir_dolares_a_pesos(dolares)
        print("El equivalente en pesos es:", pesos)
    elif opcion == 4:
        euros = float(input("Ingrese la cantidad de euros: "))
        pesos = convertir_euros_a_pesos(euros)
        print("El equivalente en pesos es:", pesos)
    elif opcion == 5:
        break
    else:
        print("Opcion no valida")   
        

















""" peso = int(input("Ingrese la cantidad de pesos chilenos: "))
dolar = float(input("Ingrese el valor actual del dolar: "))

def convertir(peso, dolar):
    return peso / dolar

dolar_a_peso = convertir(peso, dolar)
print("El equivalente en dolares es:", dolar_a_peso) """