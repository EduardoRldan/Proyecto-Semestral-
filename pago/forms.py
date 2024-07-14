from django import forms
from .models import MetodoPago, Transaccion

class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = ['nombre']

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['producto', 'metodo_pago', 'monto']
