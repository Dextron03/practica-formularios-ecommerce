from django.shortcuts import render, redirect
from . import form
from .models import Productos

# Create your views here.
def producto(request):

    if request.method == "GET":
       form_producto = form.ProductoFrom(request.GET)
       return render(request, "form_producto.html", {"form":form_producto})
   
    if request.method == "POST":
        form_producto = form.ProductoFrom(request.POST, request.FILES)
        if form_producto.is_valid():
            form_producto.save()
            return redirect('producto')
        else:
            return render(request, "form_producto.html", {"form":form_producto})
        
def home(request):
    products = Productos.objects.all()
    
    return render(request, 'index.html', {"producto":products})
    
