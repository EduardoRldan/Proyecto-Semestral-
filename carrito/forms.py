#modelo de carrito 
from django import forms
from .models import ItemCarrito,Orden 

class AgregarAlCarritoForm(forms.ModelsForm):
    class Meta:
        model = ItemCarrito
        fields = ['cantidad']

class CrearOrdenForm(forms.ModelForm):
    class Meta :
        model = Orden
        fields = []