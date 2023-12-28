from django.urls import path
from . import views

urlpatterns = [
    path('productos/',views.producto, name='productos'),
    path('', views.home,name='home')
]
