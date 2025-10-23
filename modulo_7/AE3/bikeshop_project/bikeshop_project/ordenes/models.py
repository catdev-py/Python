from django.db import models
from clientes.models import Cliente
from bicicletas.models import Bicicleta
class Orden(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,  # borrar órdenes si se elimina el cliente
        related_name='ordenes'     # acceso inverso: cliente.ordenes.all()
    )
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    estado = models.CharField(
        max_length=20,
        choices=[('pendiente','Pendiente'), ('pagada','Pagada'), ('cancelada','Cancelada')],
        default='pendiente'
    )
    
    bicicletas = models.ManyToManyField(Bicicleta, through='DetalleOrden', related_name='ordenes')
    
    def __str__(self):
        return f"Orden {self.id} - Cliente: {self.cliente.nombre}"
    
class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    bicicleta = models.ForeignKey(Bicicleta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.bicicleta.nombre} en {self.orden}"