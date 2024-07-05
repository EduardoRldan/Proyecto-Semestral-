from django.contrib import admin
from .models import Producto, Carrito, ItemCarrito, Orden
# Register your models here.

admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(Orden)