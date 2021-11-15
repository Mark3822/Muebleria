from django.db import models

# Create your models here.

class Usuario(models.Model): # MODELO USUARIO 
    usuario = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return f'Usuario:{self.id}: {self.usuario}, {self.password}' # SOBREESCRITURA DEL METODO STR PARA MUESTRA EN EL ADMIN