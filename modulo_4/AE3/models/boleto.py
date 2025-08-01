from __future__ import annotations
from typing import TYPE_CHECKING
import uuid
from datetime import datetime

# Para evitar importación circular
if TYPE_CHECKING:
    from .usuario import Usuario
    from .funcion import Funcion

class Boleto:
    def __init__(self, usuario: Usuario, funcion: Funcion, asiento: str):
        self.id_boleto = str(uuid.uuid4())
        self.usuario = usuario  # Asociación: el boleto es DE un usuario
        self.funcion = funcion  # Asociación: el boleto es PARA una función
        self.asiento = asiento
        self.fecha_compra = datetime.now()

    def __str__(self) -> str:
        """Representación detallada del boleto."""
        return (
            f"--- BOLETO CINECLUB ---\n"
            f"ID: {self.id_boleto[:8]}\n"
            f"Película: {self.funcion.pelicula.titulo}\n"
            f"Función: {self.funcion.fecha.strftime('%d/%m/%Y')} a las {self.funcion.hora.strftime('%H:%M')}\n"
            f"Sala: {self.funcion.sala}\n"
            f"Asiento: {self.asiento}\n"
            f"Comprado por: {self.usuario.nombre}\n"
            f"Fecha de compra: {self.fecha_compra.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"-----------------------"
        )