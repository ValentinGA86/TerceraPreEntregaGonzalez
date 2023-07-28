from django.db import models

# Create your models here.

class Marcas(models.Model):
    nombre = models.CharField(max_length=50)
    CLASE = (
        ("Clase 1", "Clase 1"),
        ("Clase 2", "Clase 2"),
        ("Clase 3", "Clase 3")
    )
    TIPO = (
        ("D", "Denominativa"),
        ("F", "Figurativa"),
        ("M", "Mixta")
    )
    tipo = models.CharField(max_length=50, choices=TIPO)
    clase = models.CharField(max_length=50, choices=CLASE)
    fecha = models.DateField()

class ModelosIndustriales(models.Model):
    nombre = models.CharField(max_length=50)
    clase = models.CharField(max_length=50)
    subclase = models.IntegerField()
    fecha = models.DateField()

class DiseñosIndustriales(models.Model):
    nombre = models.CharField(max_length=50)
    clase = models.CharField(max_length=50)
    subclase = models.IntegerField()
    fecha = models.DateField()
