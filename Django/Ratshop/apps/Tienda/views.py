from django.shortcuts import render,redirect
from .models import *
import os
from django.conf import settings
import json
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def iniciosesion(request):
    return render(request, 'iniciosesion.html')

def cargarInicio(request):
    productos = Producto.objects.all()
    cate_perros = Producto.objects.filter(categoria_id = 1)
    cate_gatos = Producto.objects.filter(categoria_id = 2)
    return render(request, "productoss.html",{"prod":productos, "cate_perro":cate_perros,"cate_gato":cate_gatos})



def cargarAgregarProducto(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request,"agregarProducto.html",{"cate":categorias, "prod":productos})



def agregarProducto(request):
    #print("AGREGAR PRODUCTO",request.POST)
    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtNombre']
    v_descripcion = request.POST['txtDescripcion']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    if request.POST['fechaVencimientoSel'] == "":
        v_fecha_vencimiento = None
    else:
        v_fecha_vencimiento = request.POST['fechaVencimientoSel']
    v_image = request.FILES['txtImg']
    v_categoria = Categoria.objects.get(categoria_id = request.POST['cmbCategoria'])

    Producto.objects.create(sku = v_sku, nombre= v_nombre, descripcion = v_descripcion, stock = v_stock,precio = v_precio,fecha_vencimiento = v_fecha_vencimiento, image_url = v_image, categoria_id = v_categoria )

    return redirect('/agregarProducto')





def cargarEditarProducto(request,sku):
    productos = Producto.objects.get(sku = sku)
    categorias = Categoria.objects.all()

    cateId = productos.categoria_id

    productoCategoria = Categoria.objects.get(categoria_id = cateId.categoria_id).categoria_id

    return render(request,"editarProducto.html",{"prod":productos, "cate":categorias,"categoriaId":productoCategoria})



def editarProductoForm(request):
    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(sku = v_sku)
    v_nombre = request.POST['txtNombre']
    v_descripcion = request.POST['txtDescripcion']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    if request.POST['fechaVencimientoSel'] == "":
        v_fecha_vencimiento = None
    else:
        v_fecha_vencimiento = request.POST['fechaVencimientoSel']
    v_categoria = Categoria.objects.get(categoria_id = request.POST['cmbCategoria'])


    try:
        v_image = request.FILES['txtImg']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.image_url))
        os.remove(ruta_imagen)
    except:
        v_image = productoBD.image_url


    productoBD.nombre = v_nombre
    productoBD.descripcion = v_descripcion
    productoBD.stock = v_stock
    productoBD.precio = v_precio
    productoBD.fecha_vencimiento = v_fecha_vencimiento
    productoBD.image_url = v_image
    productoBD.categoria_id = v_categoria


    productoBD.save()
    return redirect('/agregarProducto')


def eliminarProducto(request,sku):
    print("ELIMINAR PRODUCTO",sku)
    producto = Producto.objects.get(sku = sku)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.image_url))
    os.remove(ruta_imagen)
    producto.delete()
    return redirect('/agregarProducto')


def carrito(request):
    #print("CARRITO",request.body)
    data = json.loads(request.body)
    for p in data:
        print('SKU',p['sku'])
        print('CANBTIDAD',p['cantidad'])
    return HttpResponse("Ok!")

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/index')
    else:
        form = AuthenticationForm()
    
    return render(request, 'iniciosesion.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/index')
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})