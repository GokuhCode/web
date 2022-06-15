from dataclasses import field
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Producto

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields =['nombre','categoria','precio']