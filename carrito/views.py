from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito, ItemCarrito, Orden
from .forms import AgregarAlCarritoForm, CrearOrdenForm
# Create your views here.
#Vista del Carrito de compra 

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        form = AgregarAlCarritoForm(request.POST)
        if form.is_valid():
            contidad =form.cleaned_data['cantidad']
            precio_unitario = producto.precio
            item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto, precio_unitario=precio_unitario)
            if not created:
                item.cantidad += cantidad #arreglalos despues
            else:
                item.cantidad = cantidad #arreglalos despues
            item.save()
            return redirect('detalle_producto', id=producto_id)
        else:
            form = AgregarAlCarritoForm()
            return render (request, 'agregar_al_carrito.html', {'form':form})
        
    #esto ya requiere un login en la pagina
    def crear_orden(request):
        carrito, _= Carrito.objects.get_or_create(usuario=request.user)

        if request.method == 'POST':
            form = CrearOrdenForm(request.POST)
            if form.is_valid():
                items = carrito.items.all()
                total = sum(item.subtotal() for item in items)
                orden = form.save(commit=False)
                orden.usuario = request.user
                orden.total = total 
                orden.save()
                orden.items.set(items)
                carrito.items.clear()
                return redirect('ver_ordenes')
            else:
                form = CrearOrdenForm()

            return render(request, 'crear_orden.html', {'form':form})
        
    def ver_ordenes(request):
        ordenes = Orden.objects.filter(usuario=request.user)
        return render(request, 'ver_ordenes.html', {'ordenes':ordenes})
