from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. Ingresa una direccion de correo electronico valida.")

class Meta: 
    model = User
    fields = ['username', 'email', 'password1', 'password2']

def clean_email(self):
    email = self.cleaned_data.get('email')
    if User.objects.filter(email=email).exists():
        raise forms.ValidationError("Este correo ya esta registrado!, Intenta con otro")
    return email

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de Usuario', max_length=254)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)