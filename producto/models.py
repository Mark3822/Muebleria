from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.fields import IntegerField
from django.db.models.fields import FloatField

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=25)
    foto = models.CharField(max_length=30)
    def __str__(self):
        return f'Categoria {self.categoria} {self.foto}'

class Producto(models.Model):
    nombre = models.CharField(max_length=25)
    stock = models.IntegerField()
    precio = models.FloatField()
    descripcion = models.CharField(max_length=80)
    foto = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'Producto {self.nombre} {self.stock} {self.precio} {self.descripcion} {self.foto}' # SOBREESCRITURA DEL METODO STR PARA LA MUESTRA EN ADMIN

    