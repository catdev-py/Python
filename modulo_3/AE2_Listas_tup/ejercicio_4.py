""" 
Conjuntos - Operaciones Matemáticas de Conjuntos
Son similares a los sets y permiten hacer operaciones como en matemáticas: 
"""
grupo_a = {"Carlos", "Ana", "Pedro"}
grupo_b = {"Ana", "Luis", "Pedro"}

# Unión (todos sin repetir)
print(grupo_a.union(grupo_b))

# Intersección (los que están en ambos)
print(grupo_a.intersection(grupo_b))

# Diferencia (los que están en A pero no en B)
print(grupo_a.difference(grupo_b))
