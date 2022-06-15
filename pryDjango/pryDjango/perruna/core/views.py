from django.shortcuts import render
from urllib3 import HTTPResponse
from core.models import Producto
from .forms import ProductoForm


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
    
def registro_usuario(request):
    return render(request, 'registration/registrar.html')

def nuevo_producto(request):
    data = {

        'form':ProductoForm 
    }
    if request.method == 'POST':
       formulario= ProductoForm(request.POST)
       if formulario.is_valid():
           formulario.save()
           data['mensaje'] = "Guardado Correctamente"



    return render(request,'core/nuevo_producto.html' ,data)


 
