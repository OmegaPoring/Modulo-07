from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class Laboratorio(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, verbose_name="Nombre")
    city=models.CharField(max_length=50, verbose_name="Ciudad", blank=True)
    country=models.CharField(max_length=50, verbose_name="Pais", blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class DirectorGeneral(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, verbose_name="Nombre")
    laboratorio=models.OneToOneField(Laboratorio, on_delete=models.SET_NULL, null=True)
    especialidad=models.CharField(max_length=50, verbose_name="Especialidad", blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

def validador(valor):
    if valor.year < 2015:
        raise ValidationError("El año debe ser igual o posterior a 2015")

class Producto(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, verbose_name="Nombre")
    laboratorio=models.ForeignKey(Laboratorio, on_delete=models.SET_NULL, null=True)
    f_fabricacion=models.DateField(validators=[validador], verbose_name="Fecha de Fabricacion")
    p_costo=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de Costo")
    p_venta=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de Venta")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    @property
    def fecha_de_fabricacion(self):
        return self.f_fabricacion.strftime('%Y')

    def __str__(self):
        return self.name