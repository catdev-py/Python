# Función que recibe una lista de notas y devuelve el promedio
def promedio_notas(notas):
    total = sum(notas)
    cantidad = len(notas)
    promedio = total / cantidad
    return promedio

notas_mate = [5.5, 6.0, 5.8, 6.2]
prom = promedio_notas(notas_mate)
print("El promedio de notas es:", prom)
