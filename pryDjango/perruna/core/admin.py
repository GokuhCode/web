from django.contrib import admin

from core.views import productos
from .models import Producto
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','categoria', 'precio']
    search_fields = ['nombre', 'categoria', 'precio']
    list_filter= ['categoria']
admin.site.register(Producto, ProductoAdmin)