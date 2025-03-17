from django.db import models
import uuid
import os

# Create your models here.

def upload_to_galeria(instance, filename):
    ext = filename.split('.')[-1]
    unique_name = f"{uuid.uuid4().hex}.{ext}"  
    return os.path.join('galeria/', unique_name)

def upload_to_platillos(instance, filename):
    ext = filename.split('.')[-1]
    unique_name = f"{uuid.uuid4().hex}.{ext}"  
    return os.path.join('platillos/', unique_name)

def upload_to_promotions(instance, filename):
    ext = filename.split('.')[-1]
    unique_name = f"{uuid.uuid4().hex}.{ext}"  # hex elimina los guiones
    return os.path.join('promotions/', unique_name)


class Galeria(models.Model):
    imagen = models.ImageField(upload_to=upload_to_galeria, blank=True, null=True)

    def __str__(self):
        return self.imagen.url

class Promocion(models.Model):
    ruta = models.ImageField(upload_to=upload_to_promotions, blank=True, null=True)

    def __str__(self):
        return self.ruta.url

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre

class Mesa(models.Model):
    mesa = models.CharField(max_length=10)
    asientos = models.IntegerField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

class Reservacion(models.Model):
    fecha = models.DateTimeField()
    cant_personas = models.IntegerField()
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Platillo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()
    imagen = models.ImageField(upload_to=upload_to_platillos, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    visibilidad = models.BooleanField()

    def __str__(self):
        return self.nombre