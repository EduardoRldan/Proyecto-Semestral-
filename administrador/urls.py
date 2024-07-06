from django.urls import path
from .import views

urlpatterns=[
    path ('menu', views.menu, name="menu"),
    path ('reporte_administrador', views.reporte_administrador, name="reporte_administrador"),
    path ('home', views.home, name="home")
]