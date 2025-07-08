# Usando Tuplas (Datos que NO cambian)
# Las tuplas son como listas, pero no se pueden modificar
dias_semana = ("lunes", "martes", "miércoles", "jueves", "viernes")

print("Días de la semana:", dias_semana)

# Acceder a un valor
print("El primer día es:", dias_semana[0])

# Contar cuántos días hay
print("Cantidad de días:", len(dias_semana))

# Intentar modificar (esto generará un error)
# descomenta la siguiente línea para probar
# dias_semana[0] = "domingo" 
