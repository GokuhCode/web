from django.urls import path
from.views import contacto, login, producto, quienessomos, home

urlpatterns = [
        path('', home, name='home'),
          path('quienessomos/', quienessomos, name="quienessomos"),
          path('Contacto/', contacto, name="Contacto"),
           path('login/', login, name="login"),
           path('producto/', producto, name="productos"),
           

  ]