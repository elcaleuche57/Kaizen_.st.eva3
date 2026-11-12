from django.contrib import admin

from django.contrib import admin
from .models import Categoria, Prenda


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activa", "creada")
    list_filter = ("activa",)
    search_fields = ("nombre",)


@admin.register(Prenda)
class PrendaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "talla", "precio", "stock")
    list_filter = ("categoria", "talla")
    search_fields = ("nombre", "descripcion")
