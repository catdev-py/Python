# Ejemplo de sorted()
frutas = ["manzana", "plátano", "kiwi", "durazno", "Aguacate", "aguacate", "Manzana"]
frutas_ordenadas = sorted(frutas)
frutas_ordenadas_2 = sorted(frutas, reverse=True)
print("Frutas sin ordenar:", frutas)
print("Frutas ordenadas:", frutas_ordenadas)
print("Frutas ordenadas 2:", frutas_ordenadas_2)

""" frutas = ["manzana", "Manzana", "Kiwi", "durazno", "Durazno"]
ordenadas = sorted(frutas, key=str.lower)
print(ordenadas)

print(ord("M"))  # 77
print(ord("m"))  # 109 """
