from django import forms
from .models import Categoria, Producto

class CategoriaForm(forms.ModelForm):
    class Meta: 
        model = Categoria
        fields = ['nombre']

class ProductoForm(forms.modelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria']