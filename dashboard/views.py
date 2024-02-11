from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Producto, Pedido, Proveedor
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import Formulario_Producto

@login_required()
def index(request):
    title = "Gestión de Inventarios"
    return render(request, 'index.html', {'title': title})

@login_required()
def dashboard(request):
    title = "Dashboard"
    productos = Producto.objects.all()
    pedidos = Pedido.objects.all()
    cantidad_pedidos = pedidos.count()
    cantidad_productos = productos.count()
    return render(request, 'dashboard/dashboard.html', {'title': title, 'cantidad_productos': cantidad_productos, 'cantidad_pedidos': cantidad_pedidos})

@login_required
def productos(request):
    title = "Productos"
    productos = Producto.objects.all() 

    if request.method == 'POST':
        form = Formulario_Producto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos') 
    else:
        form = Formulario_Producto()

    context = {
        'productos': productos,
        'form': form,
        'title': title
    }  
    return render(request, 'dashboard/productos.html', context)

@login_required
def eliminar_producto(request, id):
    title = "Eliminar Producto"
    producto = Producto.objects.get(id=id)
    return render (request, 'dashboard/eliminar_producto.html', {'title': title})

@login_required
def editar_producto(request, id):
    title = "Actualizar Producto"
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        form = Formulario_Producto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = Formulario_Producto(instance=producto)
    context = {
        'form': form,
        'title': title
    }
    return render(request, 'dashboard/actualizar_producto.html', context)

@login_required()
def pedidos(request):
    title = "Pedidos"
    pedidos = Pedido.objects.all()
    cantidad_pedidos = pedidos.count()
    return render(request, 'dashboard/pedidos.html', {'pedidos': pedidos, 'title': title, 'cantidad_pedidos': cantidad_pedidos})

@login_required()
def clientes(request):
    title = "Clientes"
    return render(request, 'dashboard/clientes.html', {'title': title})

def logout_user(request):
    logout(request)
    return redirect('login_user')