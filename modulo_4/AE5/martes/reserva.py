# clase reserva, la fecha de resreva y de devolución debe tener día y hora
from datetime import datetime

class Reserva:
    def __init__(self, id_reserva, id_bicicleta, rut_usuario, fecha_reserva, fecha_devolucion):
        formato = "%Y-%m-%d %H:%M"  # Ajusta según cómo ingresas las fechas
        self.id_reserva = id_reserva
        self.id_bicicleta = id_bicicleta
        self.rut_usuario = rut_usuario
        self.fecha_reserva = datetime.strptime(fecha_reserva, formato)
        self.fecha_devolucion = datetime.strptime(fecha_devolucion, formato)

    def __str__(self):
        return (f"ID Reserva: {self.id_reserva}, ID Bicicleta: {self.id_bicicleta}, "
                f"Rut Usuario: {self.rut_usuario}, Fecha Reserva: {self.fecha_reserva}, "
                f"Fecha Devolucion: {self.fecha_devolucion}")
    
    def registrar_reserva(self):
        return f"ID Reserva: {self.id_reserva}, ID Bicicleta: {self.id_bicicleta}, Rut Usuario: {self.rut_usuario}, Fecha Reserva: {self.fecha_reserva}, Fecha Devolucion: {self.fecha_devolucion}"
    
    def mostrar_info(self):
        print(f"ID Reserva: {self.id_reserva}")
        print(f"ID Bicicleta: {self.id_bicicleta}")
        print(f"Rut Usuario: {self.rut_usuario}")
        print(f"Fecha Reserva: {self.fecha_reserva}")
        print(f"Fecha Devolucion: {self.fecha_devolucion}")
  
  # se calcula el valor total de la reserva, multiplicando el precio por el total de horas
    def calcular_valor(self):
        horas = (self.fecha_devolucion - self.fecha_reserva).total_seconds() / 3600
        return self.id_bicicleta.precio * horas
        
    def cancelar_reserva(self):
        print(f"Reserva cancelada. ID Reserva: {self.id_reserva}")
        
    def pagar_reserva(self):
        print(f"Reserva pagada. ID Reserva: {self.id_reserva}")