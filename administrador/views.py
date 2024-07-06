from django.shortcuts import render
from administrador.models import administrador
from django.contrib.auth.decorators import login_required

# Create your views here.
def menu(request):
    request.session["administrador"] = "eroldan"
    usuario = request.sessio["administrador"]
    context = {"administrador" : administrador}
    return render(request, "administrador/menu.html",context)

def reporte_administrador(request):
    administrador = administrador.objects.all()
    context = {"administrador":administrador}
    return render(request, "administrador/menu.html",context)

def home(request):
    context={}
    return render(request, "administrador/home.html",context)