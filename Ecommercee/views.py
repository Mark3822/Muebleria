from django.http import HttpResponse
from django.shortcuts import render
from usuario.models import Usuario
from producto.models import Producto, Categoria

# Create your views here.

def login(request):
    return render(request,'login.html')

def home(request):
    categorias = Categoria.objects.all()
    return render(request,'home.html',{'categorias':categorias})

def productos(request):
    productosxCat = Producto.objects.all()
    return render(request,'productos.html',{'productoxCat':productosxCat})
def validar(request):
    userform = request.POST.get('user')
    passform = request.POST.get('pass')
    if Usuario.objects.filter(usuario = userform, password = passform) :
        return HttpResponse("<h1 style=\" font-size: 105px; \" >EN PROCESO... OBRAS 2022  </h1> <h2></h2><h2></h2>")
    else:      
        return render(request,'login.html', {'mensaje':'Usuario o contraseña erronea'})  
      