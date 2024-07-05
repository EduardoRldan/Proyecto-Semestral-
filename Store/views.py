from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Videojuegos
from .models import VideojuegosForm
#filtro de lista de videojuegos
def lista_videojuegos(request):
    Videojuegos = Videojuegos.object.filter([
        'Assasin/s Creed',
        'Call of Duty',
        'Need for Speed: Most Wanted'
    ])

def detalle_videojuegos(request, id):
    Videojuegos = get_list_or_404(Videojuegos, id=id)
    return render (request, 'videojuegos/detalle_videojuego.html', {'videojuego':Videojuegos})

def nuevo_videojuegos(request):
    if request.method == 'POST':
        form = Videojuegos(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegosForm()
        return render(request, 'videojuegos/nuevo_videojuego.html', {'form':form})
    
def editar_videojuegos(request):
    Videojuegos = get_list_or_404(Videojuegos, id=id)
    if request.method == 'POST':
        form = VideojuegosForm(request.POST, istance=Videojuegos)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
        else:
            form = VideojuegosForm(instance=Videojuegos)
            return render (request, 'videojuegos/editar_videjuego.html', {'form':form})
        
def eliminar_videojuegos(request,id):
    Videojuegos = get_list_or_404(Videojuegos, id=id)
    if request.method == 'POST':
        Videojuegos.delete()
        return redirect('lista_videojuegos')
    return render(request, 'videojuegos/eliminar_videojuego.html', {'videojuego':Videojuegos})


