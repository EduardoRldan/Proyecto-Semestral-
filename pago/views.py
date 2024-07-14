from django.shortcuts import render, get_object_or_404, redirect
from .models import MetodoPago, Transaccion
from .forms import MetodoPagoForm, TransaccionForm

def lista_metodos_pago(request):
    metodos_pago = MetodoPago.objects.all()
    return render(request, 'tienda/lista_metodos_pago.html', {'metodos_pago': metodos_pago})

def crear_metodo_pago(request):
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_metodos_pago')
    else:
        form = MetodoPagoForm()
    return render(request, 'tienda/crear_metodo_pago.html', {'form': form})

def editar_metodo_pago(request, pk):
    metodo_pago = get_object_or_404(MetodoPago, pk=pk)
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST, instance=metodo_pago)
        if form.is_valid():
            form.save()
            return redirect('lista_metodos_pago')
    else:
        form = MetodoPagoForm(instance=metodo_pago)
    return render(request, 'tienda/editar_metodo_pago.html', {'form': form})

def eliminar_metodo_pago(request, pk):
    metodo_pago = get_object_or_404(MetodoPago, pk=pk)
    if request.method == 'POST':
        metodo_pago.delete()
        return redirect('lista_metodos_pago')
    return render(request, 'tienda/eliminar_metodo_pago.html', {'metodo_pago': metodo_pago})

def lista_transacciones(request):
    transacciones = Transaccion.objects.all()
    return render(request, 'tienda/lista_transacciones.html', {'transacciones': transacciones})

def crear_transaccion(request):
    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_transacciones')
    else:
        form = TransaccionForm()
    return render(request, 'tienda/crear_transaccion.html', {'form': form})

def editar_transaccion(request, pk):
    transaccion = get_object_or_404(Transaccion, pk=pk)
    if request.method == 'POST':
        form = TransaccionForm(request.POST, instance=transaccion)
        if form.is_valid():
            form.save()
            return redirect('lista_transacciones')
    else:
        form = TransaccionForm(instance=transaccion)
    return render(request, 'tienda/editar_transaccion.html', {'form': form})

def eliminar_transaccion(request, pk):
    transaccion = get_object_or_404(Transaccion, pk=pk)
    if request.method == 'POST':
        transaccion.delete()
        return redirect('lista_transacciones')
    return render(request, 'tienda/eliminar_transaccion.html', {'transaccion': transaccion})
