
from django import forms
from .models import Videojuego, ItemCarrito, Orden
#modelo de tienda 
class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['titulo', 'genero', 'descripcion', 'precio', 'fecha_lanzamiento']
