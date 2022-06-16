from dataclasses import field
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields =['nombre','categoria','precio']

class CustomUserForm(UserCreationForm):
    pass
