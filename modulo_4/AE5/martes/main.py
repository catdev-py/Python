from bicicleta import Bicicleta
from reserva import Reserva
from datetime import datetime




bici1 = Bicicleta(
    id=1,
    marca="Oxford",
    modelo="Dev",
    precio=1000,
    disponible=True
)

bici2 = Bicicleta(
    id=2,
    marca="Bianchi",
    modelo="K2",
    precio=2000,
    disponible=True
)

bici3 = Bicicleta(
    id=3,
    marca="Trek",
    modelo="Ever",
    precio=2000,
    disponible=True
)

reserva1 = Reserva(
    id_reserva=1,
    id_bicicleta=bici1,
    rut_usuario="12345678-9",
    fecha_reserva="2025-08-05 10:00",
    fecha_devolucion="2025-08-05 14:00"
)

print(reserva1.calcular_valor())
