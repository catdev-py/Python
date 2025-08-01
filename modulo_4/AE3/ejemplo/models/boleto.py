from datetime import datetime
import uuid

from .funcion import Funcion 
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .usuario import Usuario 

class Boleto:
    def __init__(self, usuario: 'Usuario', funcion: Funcion, asiento: str):
        self.id_boleto = str(uuid.uuid4())
        self.usuario = usuario  # Asociación: el boleto es DE un usuario
        self.funcion = funcion  # Asociación: el boleto es PARA una función
        self.asiento = asiento
        self.fecha_compra = datetime.now()
        
    def __str__(self):
        return f"Boleto de '{self.funcion.pelicula.titulo}' - Sala {self.funcion.sala} - {self.funcion.fecha.strftime('%d/%m/%Y')} a las {self.funcion.hora.strftime('%H:%M')} - Asiento {self.asiento}"
    