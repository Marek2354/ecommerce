from django.shortcuts import render, redirect
from .models import Producto

# Página de inicio: muestra el catálogo
def inicio(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/lista_productos.html', {'productos': productos})

# Vista secundaria para lista de productos (opcional)
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/lista_productos.html', {'productos': productos})

# Agregar producto al carrito
def agregar_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', [])
    carrito.append(producto_id)
    request.session['carrito'] = carrito
    return redirect('inicio')

# Ver carrito
def ver_carrito(request):
    carrito = request.session.get('carrito', [])
    productos = Producto.objects.filter(id__in=carrito)
    return render(request, 'tienda/carrito.html', {'productos': productos})

# Eliminar producto del carrito
def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', [])
    if producto_id in carrito:
        carrito.remove(producto_id)
        request.session['carrito'] = carrito
    return redirect('ver_carrito')
