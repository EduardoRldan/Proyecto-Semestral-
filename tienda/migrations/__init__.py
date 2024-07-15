from django.db import migrations

def add_initial_videojuego(apps, schema_editor):
    Videojuego = apps.get_model('tienda', 'Videojuego')
    Videojuego.objects.create(
        nombre='Call of Duty 2',
        descripcion='Un juego de disparos en Primera Persona',
        precio=60.99,
        fecha_lanzamiento='2006-11-25',
        desarrollador='Infinity Ward',
        editor='Activision',
        imagen='Static/img/cod2.jpg',
    )

    Videojuego.objects.create(
        nombre='Assasin\'s Creed',
        descripcion='Un juego de acción y aventuras',
        precio=49.99,
        fecha_lanzamiento='2007-11-16',
        desarrollador='Ubisoft Montreal',
        editor='Ubisoft',
        imagen='Static/img/assasa1.jpg',
    )

    Videojuego.objects.create(
        nombre='Need for Speed: Most Wanted',
        descripcion='Un juego de carreras',
        precio=39.99,
        fecha_lanzamiento='2005-11-11',
        desarrollador='Ghost Games',
        editor='Electronic Arts',
        imagen='Static/img/needforspped.jpg',
    )

class Migration(migrations.Migration):
    dependencies = [
        ('tienda', '0001_initial'),  # Ajusta el nombre del archivo de la migración anterior
    ]

    operations = [
        migrations.RunPython(add_initial_videojuego),
    ]
