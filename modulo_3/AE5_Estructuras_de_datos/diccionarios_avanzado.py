
# MINI-TALLER: Diccionarios anidados
# Objetivo: Usar diccionarios que contienen listas y otros diccionarios

escuela = {
    "nombre": "Coding Dojo LATAM",
    "profesores": [
        {"nombre": "Alfredo", "cursos": ["Python", "Java"]},
        {"nombre": "Valeria", "cursos": ["Fundamentos", "Java"]},
        {"nombre": "Marcelo", "cursos": ["MERN", "Python"]}
    ]
}

# Imprimir el nombre del primer profesor
print("Primer profesor:", escuela["profesores"][0]["nombre"])

# ACTIVIDAD:
# Crea un diccionario que represente una tienda con productos, cada producto debe tener:
# nombre, precio y stock.
