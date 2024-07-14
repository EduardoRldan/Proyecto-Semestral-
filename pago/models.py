from django.db import models
from django.contrib.auth.models import User
from autenticacion .models import Producto
# Create your models here.

class MetedoPago(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Transaccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetedoPago, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Transacción {self.id}- {self.usuario.username}-{self.producto.nombre}'