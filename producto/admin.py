from django.contrib import admin
from producto.models import Producto, Categoria

# Register your models here.
admin.site.register(Producto) # REGISTRO DEL MODELO DE PRODUCTO
admin.site.register(Categoria)