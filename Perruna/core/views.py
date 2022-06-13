from django.shortcuts import render
from urllib3 import HTTPResponse
from core.models import Producto

# Create your views here.
def home(request): 
    return render(request, 'core/home.html')    
def quienessomos(request): 
    return render(request, 'core/quienessomos.html')   
def contacto(request): 
    return render(request, 'core/Contacto.html')   
def login(request): 
    return render(request, 'core/login.html')    
def productos(request): 
    productos= Producto.objects.all()
    data = {
        'Productos':productos
    }
    return render(request, 'core/productos.html' ,data)    

 
