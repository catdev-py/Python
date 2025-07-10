paises = {} #Diccionario vacío

paises["MEX"] = "México" #Agregando valores

paises["COL"] = "Colombia"

paises["CHL"] = "Chile"

print(paises)

if "CRI" in paises: #Preguntamos si existe la clave en el diccionario

    print("¿Deseas reemplazar el valor?")

else: #No existe esa clave

    paises["CRI"] = "Costa Rica"
    
print(paises)

valor_removido = paises.pop("MEX") #Elimina el elemento y devuelve su valor

del paises["COL"] #Elimina el elemento

print(paises) #Imprime: {'CHL': 'Chile'}

print(paises.keys()) #Imprime: dict_keys(['CHL', 'CRI'])

print(paises.values()) #Imprime: dict_values(['Chile', 'Costa Rica'])

print(paises.items()) #Imprime: dict_items([('CHL', 'Chile'), ('CRI', 'Costa Rica')])

texto = str(paises)

print(texto)

