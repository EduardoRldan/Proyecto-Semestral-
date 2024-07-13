from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('', views.lista_videojuegos, name='lista_videojuegos'),
    path('<int:id>/', views.detalle_videojuego, name='detalle_videojuego'),
    path('nuevo/', views.nuevo_videojuego, name='nuevo_videojuego'),
    path('<int:id>/editar/', views.editar_videojuego, name='editar_videojuego'),
    path('<int:id>/eliminar/', views.eliminar_videojuego, name='eliminar_videojuego'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]