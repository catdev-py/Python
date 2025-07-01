"""
Diccionarios - Agenda de Contactos
Los diccionarios son como una agenda donde buscas algo por su nombre o clave.
"""
contactos = {
    "Marcelo": "123456789",
    "Ana": "987654321"
}

print(contactos["Ana"])  # Buscar el teléfono de Ana

# Usando get (si no existe, no da error)
print(contactos.get("Pedro", "No encontrado"))

# Ver todas las claves
print(contactos.keys())

# Ver todos los valores
print(contactos.values())

# Actualizar o agregar
contactos.update({"Pedro": "555555555"})
print(contactos)
