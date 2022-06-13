from django import views
from django.urls import path
from.views import contacto, login, productos, quienessomos, home
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', home, name='home'),
          path('quienessomos/', quienessomos, name="quienessomos"),
          path('Contacto/', contacto, name="Contacto"),
           path('login/', login, name="login"),
            path('productos/', productos, name="productos"),
      

  ]