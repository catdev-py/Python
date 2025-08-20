class Feria:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def registrar_compra(self, cliente):
        print(cliente.mostrar_resumen())