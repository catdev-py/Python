from producto import Producto
from feria import Feria
from cliente import Cliente


if __name__ == "__main__":
    try:
        # Crear productos
        papa = Producto("Papas", 1000, 50)
        tomate = Producto("Tomates", 1500, 30)

        # Crear feria y agregar productos
        feria = Feria()
        feria.agregar_producto(papa)
        feria.agregar_producto(tomate)

        # Crear cliente
        cliente = Cliente("María González", "12.345.678-9")

        # Agregar productos a la compra
        cliente.agregar_producto(papa, 5)
        cliente.agregar_producto(tomate, 3)

        # Registrar compra
        feria.registrar_compra(cliente)

    except ValueError as e:
        print("Error:", e)