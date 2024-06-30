from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import Genero,Usuario
# Create your views here.
from .forms import GeneroForm

def index(request):
    #usuario = Usuario.objects.all()
    #context = {"usuario":usuarios}
    context={}
    return render(request,"Usuario/index.html",context)

def crud(request):
    Usuarios = Usuario.objects.all()
    #alumnos = Alumno.objects.raw("SELECT * FROM alumnos_alumno")
    context = {"Usuarios":Usuario}
    return render(request,"Usuario/Usuario_list.html",context)

def alumnosAdd(request):
    if request.method != "POST":
        print(request)
        #No es un post , por lo tanto se muestra el formulario para agregar
        generos = Genero.objects.all()
        context={"generos":generos}
        return render(request,"Usuarios/Usuario_add.html",context)
    else:
        print("Entra por aqui")
        #Es un post , por lo tanto se recuperan los datos del formulario
        #y se graban en la tabla
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
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
            activo=1
        )
        obj.save()
        context = {"mensaje":"Ok , datos guardados....."}
        return render(request,"Usuario/Usuario_add.html",context)

def alumnos_del(request,pk):
    context = {}
    try:
        Usuario=Usuario.objects.get(rut=pk)

        Usuario.delete()
        mensaje = "Eliminado satisfactoriamente"
        alumnos = Usuario.objects.all()
        context = {'alumnos':alumnos , 'mensaje':mensaje}
        return render(request,"Usuarios/Usuarios_list.html",context)
    except:
        mensaje = "Error , rut no existe"
        Usuario = Usuario.objects.all()
        context = {'Usuario':Usuario , 'mensaje':mensaje}
        return render(request,"Usuarios/Usuarios_list.html",context)
    
def alumnos_findEdit(request,pk):
    
    if pk != "":
        Usuario=Usuario.objects.get(rut=pk)
        generos = Genero.objects.all()

        print(type(Usuario.id_genero.genero))

        context = {'Usuarios':Usuario,'generos':generos}

        if Usuario:
            return render(request,"Usuarios/Usuarios_edit.html",context)
        else:
            context={"mensaje":"Error, rut no existe"}
            return render(request,"Usuarios/Usuarios_edit.html",context)

def alumnosUpdate(request):
    if request.method == "POST":
        #Es un post, por lo tanto se recuperan los datos del formulario
        # y se graban en una tabla
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero = genero)
        Usuario = Usuario()
        Usuario.rut = rut
        Usuario.nombre = nombre
        Usuario.apellido_paterno = aPaterno
        Usuario.apellido_materno = aMaterno
        Usuario.fecha_nacimiento = fechaNac        
        Usuario.id_genero = objGenero
        Usuario.telefono = telefono
        Usuario.email = email
        Usuario.direccion = direccion
        Usuario.activo=1
        Usuario.save()

        generos = Genero.objects.all()
        context = { "mensaje": "Datos actualizados satisfactoriamente", "generos":generos,"Usuario":Usuario }

        return render(request,"alumnos/alumnos_edit.html",context)
    else:
        #No es un post , por lo tanto se muestra el formulario para agregar
        alumnos = Usuario.objects.all()
        context = {"Usuario":Usuario}
        return render(request,"Usuarios/Usuarios_list.html",context)
    
def crud_generos(request):
    generos = Genero.objects.all()
    #generos = Genero.objects.raw("SELECT * FROM alumnos_alumno")
    context = {"generos":generos}
    return render(request,"alumno/Generos_list.html",context)

def generosAdd(request):
    print("estoy en controlador generosAdd")
    context = {}

    if request.method == 'POST':
        print("El controlador es un post")
        form = GeneroForm(request.POST)
        print("Estoy en agregar , is_valid")
        form.save()
        #Limpiar form
        form = GeneroForm()
        context = {
            "mensaje": "Ok, Datos guardados exitosamente",
            "form":form
        }
        return render(request,"alumnos/generos_add.html",context)
    else: 
        form = GeneroForm()
        context = {'form':form}
        return render(request,"alumnos/generos_add.html",context)