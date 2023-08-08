from django.db import models

# Create your models here.

class Compra(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.tipo}"

class Venta(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.tipo}"

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.IntegerField()
    def __str__(self):
        return f"{self.tipo}, {self.nombre}"

class Alquiler(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.IntegerField()
    precio = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.tipo}, {self.precio}"

    

