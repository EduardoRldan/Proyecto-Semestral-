from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Videojuego, Carrito, CarritoItem
from .forms import VideojuegoForm

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Carrito.objects.create(usuario=user)
            login(request, user)
            return redirect('lista_videojuegos')
    else:
        form = UserCreationForm()
    return render(request, 'tienda/registro.html', {'form': form})

def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'tienda/lista_videojuegos.html', {'videojuegos': videojuegos})

def detalle_videojuego(request, id):
    videojuego = get_object_or_404(Videojuego, id=id)
    return render(request, 'tienda/detalle_videojuego.html', {'videojuego': videojuego})

@login_required
def nuevo_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm()
    return render(request, 'tienda/nuevo_videojuego.html', {'form': form})

@login_required
def editar_videojuego(request, id):
    videojuego = get_object_or_404(Videojuego, id=id)
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, request.FILES, instance=videojuego)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm(instance=videojuego)
    return render(request, 'tienda/editar_videojuego.html', {'form': form})

@login_required
def eliminar_videojuego(request, id):
    videojuego = get_object_or_404(Videojuego, id=id)
    if request.method == 'POST':
        videojuego.delete()
        return redirect('lista_videojuegos')
    return render(request, 'tienda/eliminar_videojuego.html', {'videojuego': videojuego})

@login_required
def agregar_al_carrito(request, id):
    videojuego = get_object_or_404(Videojuego, id=id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    carrito_item, created = CarritoItem.objects.get_or_create(carrito=carrito, videojuego=videojuego)
    carrito_item.cantidad += 1
    carrito_item.save()
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    items = CarritoItem.objects.filter(carrito=carrito)
    return render(request, 'tienda/ver_carrito.html', {'items': items})

@login_required
def eliminar_del_carrito(request, id):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    item = get_object_or_404(CarritoItem, carrito=carrito, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('ver_carrito')
    return render(request, 'tienda/eliminar_del_carrito.html', {'item': item})