from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Meta:
        permissions = [
            ("view_ventas", "Puede ver la sección de ventas"),
            ("view_compras", "Puede ver la sección de compras"),
            ("view_inventarios", "Puede ver la sección de inventarios"),            
        ]

