from django.db import models
from django.core import validators

# TODO: Cambiar la ruta de las imagenes.
class Productos(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=True)
    descripcion = models.TextField(max_length=1500, null=False, blank=True)
    stock = models.PositiveBigIntegerField(default=0, null=False, blank=True, help_text="Cantidad que tiene disponible", validators=[validators.MinValueValidator(0)])
    precio = models.DecimalField(max_digits=8, decimal_places=2,null=False, blank=True, help_text="El precio del producto.", validators=[validators.MinValueValidator(0)])
    categoria = models.CharField(max_length=75, null=False, blank=True)
    imagen = models.ImageField(upload_to='media/img_productos', null=False, blank=True)
    marca = models.CharField(max_length=100, null= False, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True, null=False, blank=True)
    disponible = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.nombre
    