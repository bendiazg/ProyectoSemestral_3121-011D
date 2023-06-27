from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('iniciosesion', views.iniciosesion, name='iniciosesion'),
    path('productoss',views.cargarInicio),
    path('agregarProducto',views.cargarAgregarProducto),
    path('agregarProductoForm',views.agregarProducto),

    path('editarProducto/<sku>',views.cargarEditarProducto),
    path('editarProductoForm',views.editarProductoForm),
    path('eliminarProducto/<sku>',views.eliminarProducto),
    path('carrito',views.carrito)
]