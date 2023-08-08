from django.urls import path, include
from .views import *

urlpatterns = [

    path('', index, name="inicio"),

    path('alquileres/', alquileres, name="alquileres"),
    path('compras/', compras, name="compras"),
    path('ventas/', ventas, name="ventas"),
    

    path('equipo_form/', equipoForm, name="equipo_form"),
    path('equipo_form2/', equipoForm2, name="equipo_form2"),
    path('alquiler_form/', alquilerForm, name="alquiler_form"),
    path('alquiler_form2/', alquilerForm2, name="alquiler_form2"),

    path('buscar_precio/', buscarPrecio, name="buscar_precio"),
    path('buscar2/', buscar2, name="buscar2"),

    path('update_alquiler/<id_alquiler>', updateAlquiler, name="update_alquiler"),
    path('delete_alquiler/<id_alquiler>', deleteAlquiler, name="delete_alquiler"),
    path('create_alquiler/', createAlquiler, name="create_alquiler"),

    path('equipos/', EquipoList.as_view(), name="equipos"),
    path('create_equipo/', EquipoCreate.as_view(), name="create_equipo"),
    path('detail_equipo/', EquipoDetail.as_view(), name="detail_equipo")

]