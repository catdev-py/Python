# Variable global
contador = 0

def incrementar():
    global contador
    contador += 1

def resetear_si_es_multiplo_de_cinco():
    global contador
    if contador % 5 == 0 and contador != 0:
        contador = 0

# Programa principal
for i in range(10):
    incrementar()
    resetear_si_es_multiplo_de_cinco()
    print(f"Iteración {i+1}: contador = {contador}") 


##############################!SECTION
""" def incrementar(contador):
    return contador + 1

def resetear_si_es_multiplo_de_cinco(contador):
    if contador % 5 == 0 and contador != 0:
        return 0
    return contador

# Programa principal
contador = 0
for i in range(10):
    contador = incrementar(contador)
    contador = resetear_si_es_multiplo_de_cinco(contador)
    print(f"Iteración {i+1}: contador = {contador}") """
