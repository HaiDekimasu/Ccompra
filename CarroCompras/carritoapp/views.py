from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Carrito, CarritoItem

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'carritoapp/lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'carritoapp/detalle_producto.html', {'producto': producto})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_id = request.session.get('carrito_id')
    if not carrito_id:
        carrito = Carrito.objects.create()
        request.session['carrito_id'] = carrito.id
    else:
        carrito = Carrito.objects.get(id=carrito_id)
    
    carrito_item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        carrito_item.cantidad += 1
    carrito_item.save()
    return redirect('detalle_producto', producto_id=producto.id)

def ver_carrito(request):
    carrito_id = request.session.get('carrito_id')
    if not carrito_id:
        carrito = None
    else:
        carrito = Carrito.objects.get(id=carrito_id)
    return render(request, 'carritoapp/ver_carrito.html', {'carrito': carrito})
