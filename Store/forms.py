from django import forms 
from .models import Videojuegos

class VideojuegosFrom(forms.ModelForm):
    class Meta:
        model = Videojuegos
        fields = ['titulo', 'genero', 'descripcion', 'precio', 'fecha_lanzamiento']
        