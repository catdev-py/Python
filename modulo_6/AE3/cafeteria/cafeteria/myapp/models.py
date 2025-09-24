from django.db import models

class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='imgs/', null=True, blank=True)

class Barista(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    foto = models.ImageField(upload_to='imgs/', null=True, blank=True)

class Cafe(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    nivel_tostado = models.CharField(max_length=50)
    perfil_sabor = models.TextField()
    imagen = models.ImageField(upload_to='imgs/', null=True, blank=True)

class Resena(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    calificacion = models.IntegerField()
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
