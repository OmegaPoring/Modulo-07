from django.urls import path
from . import views

urlpatterns = [
    path("", views.labs, name="index"),
    path("agregar/", views.agregar, name="agregar"),
    path("confirmar/<int:id>/", views.confirmar, name="confirmar"),
     path("eliminar/<int:id>/", views.eliminar, name="eliminar"),
    path("actualizar/<int:id>/", views.actualizar, name="actualizar"),
]
