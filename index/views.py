from django.shortcuts import render,  get_object_or_404, redirect  
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.template import loader
from django.views import generic 
from django.views.generic import View
from django.views.generic.edit import CreateView ,  DeleteView , UpdateView
from .models import Barbero , Galeria , Producto
from django.contrib.auth import authenticate , login
from .forms import UserForm
class IndexView(generic.ListView):
    template_name = 'productos/productos.template.html'
    def get_queryset(self):
        return Producto.objects.all()
class DetailView(generic.DetailView):
      model = Producto
      template_name = 'productos/details.template.html'
class ProductCreate(CreateView):
      model = Producto 
      fields = ['nombre_producto' , 'tipo_producto' , 'marca_producto' , 'precio_unitario_producto', 'stock_producto' , 'imagen_producto']
class ProductUpdate(UpdateView):
      model = Producto 
      fields = ['nombre_producto' , 'tipo_producto' , 'marca_producto' , 'precio_unitario_producto', 'stock_producto' , 'imagen_producto']      
class ProductDelete(DeleteView): 
      model = Producto 
      success_url  =  reverse_lazy('index:product-delete')
# Create your views here.
def index(request):
    return render(request , 'index/index.template.html')
def about(request): 
    barberos = Barbero.objects.all()
    template = loader.get_template('index/about.template.html')
    context = {
        'barberos' : barberos
    }
    return HttpResponse(template.render(context ,request))
def gallery(request): 
    imagenes =  Galeria.objects.all()
    template = loader.get_template('index/gallery.template.html')
    context = {
        'imagenes' : imagenes
    }  
    return HttpResponse(template.render(context,request))
def login_user(request):
    return 0
def logout_user(request):
    return 0
def register_user(request):
    return 0