from datetime import datetime, date, time
from .pelicula import Pelicula

class Funcion:
    
    funciones = []
        
    def __init__(self, pelicula, fecha, hora, sala, asientos_disponibles):
        self.pelicula = pelicula
        
        # Si fecha es string, convertir a date, si no asumir que ya es date
        if isinstance(fecha, str):
            self.fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        elif isinstance(fecha, date):
            self.fecha = fecha
        else:
            raise TypeError("fecha debe ser str o datetime.date")
        
        # Si hora es string, convertir a time, si no asumir que ya es time
        if isinstance(hora, str):
            self.hora = datetime.strptime(hora, "%H:%M").time()
        elif isinstance(hora, time):
            self.hora = hora
        else:
            raise TypeError("hora debe ser str o datetime.time")
        
        self.sala = sala
        self.asientos_disponibles = int(asientos_disponibles)
        self.boletos_vendidos = []

        Funcion.funciones.append(self)
        
    def __str__(self):
        return f"Función de '{self.pelicula.titulo}' - Sala {self.sala} - {self.fecha.strftime('%d/%m/%Y')} a las {self.hora.strftime('%H:%M')}"
    
    @classmethod
    def consultar_horarios(cls):
        if not cls.funciones:
            print("No hay funciones disponibles.")
            return
        for funcion in cls.funciones:
            print(funcion)
        
    def obtener_disponibilidad(self):
        return self.asientos_disponibles
        
    def reservar_asiento(self, cantidad=1) -> bool:
        if self.asientos_disponibles >= cantidad:
            self.asientos_disponibles -= cantidad
            print(f"Reserva exitosa para {cantidad} asiento(s). Quedan {self.asientos_disponibles} disponibles.")
            return True
        else:
            print(f"No hay suficientes asientos disponibles. Solo quedan {self.asientos_disponibles}.")
            return False

