from django.urls import path
from .import views

urlpatterns = [
    path('metodos_pago/', views.lista_metodos_pago, name='lista_metodos_pago'),
    path('metodos_pago/crear/', views.crear_metodo_pago, name='crear_metodo_pago'),
    path('metodos_pago/editar/<int:pk>/', views.editar_metodo_pago, name='editar_metodo_pago'),
    path('metodos_pago/eliminar/<int:pk>/', views.eliminar_metodo_pago, name='eliminar_metodo_pago'),
    path('transacciones/', views.lista_transacciones, name='lista_transacciones'),
    path('transacciones/crear/', views.crear_transaccion, name='crear_transaccion'),
    path('transacciones/editar/<int:pk>/', views.editar_transaccion, name='editar_transaccion'),
    path('transacciones/eliminar/<int:pk>/', views.eliminar_transaccion, name='eliminar_transaccion'),
]