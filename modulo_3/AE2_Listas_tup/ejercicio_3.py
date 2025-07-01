""" 
Sets - La Caja de Pelotas sin Repetidos
Un set es como una caja donde tiras pelotas, 
pero no se repiten, y el orden da igual. 
"""
pelotas = {"roja", "azul", "verde", "roja"}

print(pelotas)  # Solo una roja

# Agregar una pelota nueva
pelotas.add("amarilla")
print(pelotas)

# Eliminar una pelota
pelotas.remove("azul")
print(pelotas)
