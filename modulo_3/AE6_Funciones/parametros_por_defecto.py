# Ejemplo de parámetros por defecto

def buenos_dias(nombre="alegría", cantidad=1):
    print(("Buenos días " + nombre + "\n") * cantidad)

# Llamadas a la función
buenos_dias()                                # Buenos días alegría (1 vez)
buenos_dias("al amor")                       # Buenos días al amor (1 vez)
buenos_dias(nombre="a la vida")              # Buenos días a la vida (1 vez)
buenos_dias(cantidad=3)                      # Buenos días alegría (3 veces)
buenos_dias(nombre="señor Sol", cantidad=2)  # Buenos días señor Sol (2 veces)
buenos_dias(cantidad=3, nombre="para vos")   # Buenos días para vos (3 veces)
