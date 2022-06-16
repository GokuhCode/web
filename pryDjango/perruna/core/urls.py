from django import views
from django.urls import path
from.views import base, contacto, eliminar_producto, login, modificar_producto, productos, quienessomos, home, nuevo_producto
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', home, name='home'),
           path('base/', base, name="base"),
          path('quienessomos/', quienessomos, name="quienessomos"),
          path('Contacto/', contacto, name="Contacto"),
           path('login/', login, name="login"),
            path('productos/', productos, name="productos"),
              path('nuevo-producto/', nuevo_producto, name="nuevo_producto"),
                path('modificar_producto/<id>/', modificar_producto, name="modificar_producto"),
              path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto")
                  
      

  ]