# Buscador de palabras en un texto

texto = input("Ingrese un texto largo: ").lower()
palabras = texto.split()

while True:
    buscar = input("Palabra a buscar (o 'salir'): ").lower()
    if buscar == "salir":
        break
    cantidad = palabras.count(buscar)
    print(f"La palabra '{buscar}' aparece {cantidad} veces.")