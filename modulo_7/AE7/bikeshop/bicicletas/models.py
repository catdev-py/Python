from django.db import models

class Bicicleta(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)   # mtb, ruta, enduro, trail, bmx
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    anio = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo}"