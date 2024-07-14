from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .models import UserProfile


class RegistroUsuarioForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    birth_date = forms.DateField(required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'full_name', 'birth_date', 'address')

class InicioSesionForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Guardar información adicional en UserProfile
            UserProfile.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                birth_date=form.cleaned_data['birth_date'],
                address=form.cleaned_data['address']
            )
            login(request, user)
            return redirect('perfil')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = InicioSesionForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('perfil')
    else:
        form = InicioSesionForm()
    return render(request, 'inicio_sesion.html', {'form': form})