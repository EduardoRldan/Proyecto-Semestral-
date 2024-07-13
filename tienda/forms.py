from django import forms
from .models import Videojuego

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['nombre', 'descripcion', 'precio', 'fecha_lanzamiento', 'desarrollador', 'editor', 'imagen']
