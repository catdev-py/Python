# Diccionarios, datos con claves
# Diccionario de datos de un estudiante
estudiante = {
    "nombre": "Camila",
    "edad": 16,
    "curso": "Python inicial"
}

print("Datos del estudiante:", estudiante)

# Acceder a un valor
print("El nombre es:", estudiante["nombre"])

# Modificar un valor
estudiante["edad"] = 17
print("Edad actualizada:", estudiante)

# Agregar un nuevo dato
estudiante["ciudad"] = "Temuco"
print("Después de agregar ciudad:", estudiante)

# Eliminar un dato
del estudiante["curso"]
print("Después de eliminar el curso:", estudiante)
