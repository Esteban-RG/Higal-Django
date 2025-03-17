# signals.py
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Galeria, Promocion, Platillo

@receiver(post_delete, sender=Galeria)
def eliminar_archivo_imagen(sender, instance, **kwargs):
    if instance.imagen:
        instance.imagen.delete(save=False)

@receiver(post_delete, sender=Promocion)
def eliminar_archivo_imagen(sender, instance, **kwargs):
    if instance.ruta:
        instance.ruta.delete(save=False)

@receiver(post_delete, sender=Platillo)
def eliminar_archivo_imagen(sender, instance, **kwargs):
    if instance.imagen:
        instance.imagen.delete(save=False)