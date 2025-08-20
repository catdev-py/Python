class Producto:
    def __init__(self, nombre, precio_kilo, stock):
        self.nombre = nombre
        self.precio_kilo = precio_kilo
        self.stock = stock

    def actualizar_stock(self, cantidad):
        if cantidad > self.stock:
            raise ValueError(f"Stock insuficiente para {self.nombre}")
        self.stock -= cantidad
