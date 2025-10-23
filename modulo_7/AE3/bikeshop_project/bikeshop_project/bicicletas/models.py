from django.db import models

class Bicicleta(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    tipo = models.CharField(
        max_length=20,
        choices=[('mtb', 'Montaña'), ('ruta', 'Ruta'), ('bmx', 'BMX')],
        default='mtb'
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    anio = models.IntegerField()
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"