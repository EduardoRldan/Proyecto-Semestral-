from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login (request, user)
            return redirect('perfil')
    else:
        form = UserCreationForm()
    return render (request, 'registro.html', {'form':form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('perfil')
        
    else:
        form = AuthenticationForm()
    return render (request, 'inicio_sesion.html', {'form':form})

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')


def perfil_usuario(request):
    return render (request, 'perfil.html')
