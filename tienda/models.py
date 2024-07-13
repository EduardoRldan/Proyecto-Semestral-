from django.db import models
from django.db import migrations
from django.contrib.auth.models import User

class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    desarrollador = models.CharField(max_length=100)
    editor = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes_videojuegos/')

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    videojuegos = models.ManyToManyField(Videojuego, through='CarritoItem')

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} de {self.videojuego.nombre} en el carrito de {self.carrito.usuario.username}"


def add_initial_Videjuego(apps, schema_editor):
    Videojuego = apps.get_model('videojuegos', 'Videojuego')
    Videojuego.objects.create(
        nombre = 'Call of Duty 2',
        descripcion = 'Un juego de disparos en Primera Persona',
        precio = 60.99,
        fecha_lanzamiento = '2006-11-25',
        editor = 'Activision',
        imagen = 'Static/img/cod2.jpg',
        )
    

    Videojuego.objects.created(
        nombre = 'Assasin\'s Creed',
        descripcion = 'Un juego de accion y aventuras',
        precio = 49.99, 
        fecha_lanzamiento = '2007/11/16',
        editor = 'Ubisoft',
        imagen = 'Static/img/assasa1.jpg',

    )

    Videojuego.objects.create(
        nombre = 'Need for Speed: Most Wanted',
        descripcion = 'Un juego de Carreras',
        precio = 39.99,
        fecha_lanzamiento = '2005/11/11',
        desarrollador = 'Ghost Games',
        editor = 'Electronic Arts',
        imagen = 'Static/img/needforspped.jpg'
    )

class Migration(migrations.Migration):

    dependencies =[
        ('videojuegos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_Videjuego),
    ]