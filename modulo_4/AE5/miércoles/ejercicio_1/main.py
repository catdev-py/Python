from arriendo import Arriendo
from kayak import Kayak


if __name__ == "__main__":
    try:
        kayak1 = Kayak("K001", 2, "Rojo")
        arriendo1 = Arriendo("A001", "Juan Pérez", 3, 5000, kayak1)
        print(arriendo1.mostrar_resumen())
    except ValueError as e:
        print("Error:", e)
