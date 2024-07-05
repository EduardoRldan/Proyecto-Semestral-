from django.urls import path
from .views import registro_usuario, inicio_sesion, cerrar_sesion

urlpatterns = [
    path ('registro/', registro_usuario, name='registro'),
    path ('login/', inicio_sesion,name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]