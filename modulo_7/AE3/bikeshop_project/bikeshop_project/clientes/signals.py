# clientes/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cliente, PerfilCliente

@receiver(post_save, sender=Cliente)
def crear_perfil_cliente(sender, instance, created, **kwargs):
    if created:
        PerfilCliente.objects.create(cliente=instance)