from django.db import models

from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    descripcion = models.TextField(blank=True)
    activa = models.BooleanField(default=True)
    creada = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Prenda(models.Model):
    TALLAS = [("XS", "XS"), ("S", "S"), ("M", "M"), ("L", "L"), ("XL", "XL")]

    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="prendas"
    )
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    talla = models.CharField(max_length=2, choices=TALLAS)
    stock = models.PositiveIntegerField(default=0)
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
