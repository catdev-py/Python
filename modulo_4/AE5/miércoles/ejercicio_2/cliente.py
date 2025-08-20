import re

class Cliente:
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut
        self.compras = []
        self.validar_rut()

    def validar_rut(self):
        patron = r'^\d{1,2}\.\d{3}\.\d{3}-[0-9kK]$'
        if not re.match(patron, self.rut):
            raise ValueError("RUT inválido")

    def agregar_producto(self, producto, cantidad):
        producto.actualizar_stock(cantidad)
        self.compras.append((producto, cantidad))

    def calcular_total(self):
        return sum(producto.precio_kilo * cantidad for producto, cantidad in self.compras)

    def mostrar_resumen(self):
        detalle = "\n".join([f"{producto.nombre}: {cantidad}kg - ${producto.precio_kilo * cantidad:,.0f}"
                             for producto, cantidad in self.compras])
        return (f"Cliente: {self.nombre} (RUT: {self.rut})\n"
                f"Detalle de compra:\n{detalle}\n"
                f"Total a pagar: ${self.calcular_total():,.0f}")