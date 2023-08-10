from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Register your models here.
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ['id']

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'laboratorio')
    ordering = ['id']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'laboratorio', 'fecha_de_fabricacion', 'p_costo', 'p_venta')
    ordering = ['id']

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)