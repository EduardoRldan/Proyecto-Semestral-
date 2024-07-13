from django.db import migrations

def add_initial_videojuego(apps, schema_editor):
    Videojuego = apps.get_model('tienda', 'Videojuego')
    Videojuego.objects.create(
        nombre='Call of Duty 2',
        descripcion = 'Un juego de disparos en Primera Persona',
        precio = 60.99,
        fecha_lanzamiento = '2006-11-25',
        desarrollador = 'Infinty Ward',
        editor = 'Activision',
        imagen = 'Static/img/cod2.jpg',
    )


    Videojuego.objects.create(
        nombre = 'Assasin\'s Creed',
        descripcion = 'Un juego de accion y aventuras',
        precio = 49.99,
        fecha_lanzamiento = '2007-11-16',
        editor = 'Ubisoft',
        imagen = 'Static/img/assasa1.jpg',
    )

    Videojuego.objects.create(
        nombre = 'Need for Speed: Most Wanted',
        descripcion = 'Un juego de Carreras',
        precio = 39.99,
        fecha_lanzamiento = '2005-11-11',
        desarrollador = 'Ghost Games',
        editor = 'Electronic Arts',
        imagen = 'Static/img/needforspped.jpg',
    )


class Migration(migrations.Migration):
    dependencies =[
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_videojuego),
    ]