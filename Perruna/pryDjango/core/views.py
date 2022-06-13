from django.shortcuts import render
from urllib3 import HTTPResponse

# Create your views here.
def home(request): 
    return render(request, 'core/home.html')    
def quienessomos(request): 
    return render(request, 'core/quienessomos.html')   
def contacto(request): 
    return render(request, 'core/Contacto.html')   
def login(request): 
    return render(request, 'core/login.html')    
def producto(request):
    #return render(request, 'core/productos.html' )
    productos = Producto.objects.all()
    return render(request, "productos.html",{'productos':productos})
    
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("CarritoApp: core")

def eliminar_producto(request, producto_id):
    carrito =  Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("CarritoApp: core")

def restar_producto(request, producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("CarritoApp: core")

def limpiar_carrito(request):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("CarritoApp: core")





