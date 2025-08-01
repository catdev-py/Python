from .boleto import Boleto
from typing import List, Optional, Union # qué significa esta linea de codigo
# typing es un modulo que viene con python y nos permite trabajar con type hints en python
# type hints nos permite especificar el tipo de datos que vamos a usar en nuestro codigo
# Con List nos permite trabajar con listas

class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self._password = password
        self.boletos: List[Boleto] = []

    def __str__(self):
        return f"Usuario: {self.nombre} ({self.email})"

    def registrarse(self, password):
        self._password = password  # Aseguramos acceso solo controlado
        print(f"{self.nombre} se ha registrado.")

    def comprar_boleto(self, funcion, cantidad=1) -> List[Boleto] | None:
        print(f"\n{self.nombre} intenta comprar {cantidad} boleto(s) para: {funcion}")

        # Verificamos si hay asientos disponibles
        if funcion.asientos_disponibles >= cantidad:
            nuevos_boletos = []

            for i in range(cantidad):
                # Ejemplo: asiento A-1, A-2, B-1, etc.
                fila = chr(65 + len(funcion.boletos_vendidos) // 8)
                numero = len(funcion.boletos_vendidos) % 8 + 1
                asiento = f"{fila}-{numero}"

                nuevo_boleto = Boleto(self, funcion, asiento)
                self.boletos.append(nuevo_boleto)
                funcion.boletos_vendidos.append(nuevo_boleto)

                nuevos_boletos.append(nuevo_boleto)

            funcion.asientos_disponibles -= cantidad  # Actualizamos disponibilidad
            print(f"¡Compra realizada! {self.nombre} adquirió {cantidad} boleto(s).")
            return nuevos_boletos
        else:
            print(f"No hay suficientes asientos disponibles para {cantidad} boleto(s).")
            return None

    def consultar_horario(self, funcion):
        print(f"{self.nombre} consulta el horario de la función: {funcion}")