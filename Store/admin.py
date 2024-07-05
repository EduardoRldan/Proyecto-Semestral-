# admin.py

from django.contrib import admin
from .models import Videojuego
#admin tienda 
@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'precio', 'fecha_lanzamiento')
    list_filter = ('genero', 'fecha_lanzamiento')
    search_fields = ('titulo', 'descripcion')
    fieldsets = (
        (None, {
            'fields': ('titulo', 'genero', 'descripcion')
        }),
        ('Información adicional', {
            'fields': ('precio', 'fecha_lanzamiento')
        }),
    )
    readonly_fields = ('fecha_lanzamiento',)

    def has_delete_permission(self, request, obj=None):
        return False  # Impide eliminar videojuegos desde el admin

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(titulo__in=[
            'Assassin\'s Creed', 
            'Call of Duty', 
            'Need for Speed: Most Wanted'
        ])
        return qs
    
#admin carrito 
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'creado_en')

class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ('carrito', 'videojuegos', 'cantidad', 'precio_unitario')

class OrdenAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'total', 'creada_en', 'completada')
    filter_vertical = ('items',)