from django.db import models

# Create your models here.

class Galeria(models.Model):
    imagen = models.ImageField(upload_to='galeria/', blank=True, null=True)

    def __str__(self):
        return self.imagen.url

class Promocion(models.Model):
    ruta = models.ImageField(upload_to='promotions/', blank=True, null=True)

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
    imagen = models.ImageField(upload_to='platillos/', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    visibilidad = models.BooleanField()

    def __str__(self):
        return self.nombre