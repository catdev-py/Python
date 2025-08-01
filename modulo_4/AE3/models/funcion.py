from __future__ import annotations
from typing import TYPE_CHECKING
import uuid
from datetime import date, time

# Para evitar importación circular con type hints
if TYPE_CHECKING:
    from .pelicula import Pelicula
    from .boleto import Boleto

class Funcion:
    def __init__(self, pelicula: Pelicula, fecha: date, hora: time, sala: int, asientos_disponibles: int):
        self.id_funcion = str(uuid.uuid4())
        self.pelicula = pelicula  # Relación de Composición: una función es DE una película
        self.fecha = fecha
        self.hora = hora
        self.sala = sala
        self.asientos_disponibles = asientos_disponibles
        self.boletos_vendidos: list[Boleto] = []

    def obtener_disponibilidad(self) -> int:
        """Devuelve el número de asientos disponibles."""
        return self.asientos_disponibles

    def reservar_asiento(self, cantidad: int = 1) -> bool:
        """Reserva uno o más asientos si hay disponibilidad."""
        if self.asientos_disponibles >= cantidad:
            self.asientos_disponibles -= cantidad
            print(f"Reserva exitosa para {cantidad} asiento(s). Quedan {self.asientos_disponibles} disponibles.")
            return True
        else:
            print(f"No hay suficientes asientos disponibles. Solo quedan {self.asientos_disponibles}.")
            return False

    def __str__(self) -> str:
        """Representación de la función para el usuario."""
        return f"Función de '{self.pelicula.titulo}' - Sala {self.sala} - {self.fecha.strftime('%d/%m/%Y')} a las {self.hora.strftime('%H:%M')}"