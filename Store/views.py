from django.shortcuts import render 
from .models import Genero, Usuario 

from .forms import GeneroFrom

def index(request) : 
    usuario = Usuario.object.all()
    context={"usuario":usuario}
    return render(request, "Usuario/index.html",context)

def crud (request):
    usuario = Usuario.object.all()
    context = {"usuarios":usuario}
    return render (request, "usuarios/usuarios_list.html",context)

def usuariosAdd(request):
    if request.method != "POST" :
        generos = Genero.objects.all()
        context={"generos":generos}
        return render (request, "usuarios/usuarios_add.html",context)
    
    else:
        generos = Genero.objects.all()

        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST ["fechaNac"]
        genero = request.POST ["genero"]
        telefono = request.POST ["telefono"]
        email = request.POST ["email"]
        direccion = request.POST ["direccion"]
        activo = "1"


        objGenero = Genero.objects.get(id_genero = genero)
        obj=Usuario.objects.create(

            rut = rut,
            nombre = nombre,
            apellido_paterno = aPaterno,
            apellido_materno = aMaterno,
            fecha_nacimiento = fechaNac, 
            id_genero = objGenero, 
            telefono = telefono, 
            email = email, 
            direccion = direccion, 
            activo =1 
        )
        obj.save()
        context = {"mensaje":"ok, datos guardados...","generos":generos}
        return render (request, "usuarios/usurios_add.html", context)
    
    def usuarios_del(resquest, pk): 
        context = {}
    try:
        usuario = Usuario.objects.get(rut=pk)

        Usuario.delete()

        mensaje = "Eliminado Satisfactioramente"
        usuario = Usuario.objects.all()
        context = {"usuario": Usuario, "mensaje": mensaje}
        return render(request, "usuario/usuario_list.html",context)
    
    def usuario_findEdit(request, pk):
        if pk != "":
            Usuario=Usuario.objects.get(rut=pk)
            generos = Genero.objects.all()

            print(type(Usuario.id_genero.genero))

            context = {'usuario': usuario, 'generos':generos}

            if usuario:
                return render (request, "usuario/usuario_edit.html",context)
            else: 
                context={"mensaje": "Error, rut no existente"
                         }