# Generated by Django 4.1.2 on 2024-07-14 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desarrollador', models.CharField(max_length=100)),
                ('editor', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='imagenes_videojuegos/')),
                ('fecha_lanzamiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CarritoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.carrito')),
                ('videojuego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.videojuego')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='videojuegos',
            field=models.ManyToManyField(through='tienda.CarritoItem', to='tienda.videojuego'),
        ),
    ]
