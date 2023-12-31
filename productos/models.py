from django.db import models
from django.core import validators
from django.utils.html import format_html
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Productos(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=True)
    descripcion = models.TextField(max_length=1500, null=False, blank=True)
    stock = models.PositiveBigIntegerField(
        default=0,
        null=False,
        help_text="Cantidad que tiene disponible",
        validators=[validators.MinValueValidator(0)],
        error_messages={
            'min_value': format_html('<div class="alert alert-danger" role="alert">A simple danger alert—check it out!</div>')
        }
    )
    precio = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=True,
        help_text="El precio del producto.",
        validators=[validators.MinValueValidator(0)],
        error_messages={'min_value': format_html('<div class="alert alert-danger" role="alert"> Ingrese un valor mayor o igual a cero. </div>' )}
    )
    categoria = models.CharField(max_length=75, null=False, blank=True)
    imagen = models.ImageField(upload_to='img_productos', null=False, blank=True)
    marca = models.CharField(max_length=100, null=False, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True, null=False, blank=True)
    disponible = models.BooleanField(default=True)

    def clean(self):
        # Verificar si stock es 0 y establecer disponible a False
        if self.stock == 0:
            self.disponible = False

        # Lanzar una excepción si es necesario
        if self.stock < 0 and not self.disponible:
            raise ValidationError("El stock de productos no puede ser menor a 0 si el producto no está disponible.")

    def save(self, *args, **kwargs):
        # Asegurarse de que el stock no sea negativo antes de guardar
        if self.stock is not None and self.stock < 0:
            raise ValidationError("El stock de productos no puede ser menor a 0.")

        super().save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.nombre


