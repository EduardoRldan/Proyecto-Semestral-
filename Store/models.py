from django.db import models

# Create your models here.
class Videojuegos(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_lanzamiento = models.DateField()

    def __str__(self):
        return self.titulo 