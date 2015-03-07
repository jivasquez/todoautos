from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=200)
    
class Auto(models.Model):
    titulo = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca)
    fecha_publicacion = models.DateTimeField('date published')