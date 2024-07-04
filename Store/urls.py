from django.urls import path 
from .import views

urlpatterns = [
    path('', views.lista_videojuegos, name='lista_videojuegos'),
    path('<int:id>/', views.detalle_videojuegos, name='detale_videojuegos'),
    path('nuevo/', views.nuevo_videojuegos, name='nuevo_videojuegos'),
    path('<int:id>/editar/', views.editar_videojuegos, name='editar_videojuegos'),
    path('<int:id/eliminar/>', views.eliminar_videojuegos, name='eliminar_videojuegos')
]