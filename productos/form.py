from django import forms
from . import models
from django.utils.html import format_html
class ProductoFrom(forms.ModelForm):
    class Meta:
        model = models.Productos
        fields = ['nombre', 'descripcion', 'stock', 'precio', 'categoria', 'imagen', 'marca']
        widgets = {
            'nombre':forms.TextInput(attrs={"class":"form-control mb-5"}),
            'descripcion':forms.Textarea(attrs={"class":"form-control mb-5"}),
            'stock':forms.NumberInput(attrs={"class":"form-control mb-5"}),
            'precio':forms.NumberInput(attrs={"class":"form-control mb-5"}),
            'categoria':forms.TextInput(attrs={"class":"form-control mb-5"}),
            'imagen':forms.FileInput(attrs={"class":"form-control mb-5"}),
            'marca':forms.TextInput(attrs={"class":"form-control mb-5"}),
                   }
    
    # TODO: Validar todo los campos del formulario.
    def clean_stock(self):
        stock = self.cleaned_data.get("stock")
        disponible = self.cleaned_data.get("disponible")
        
        if stock is not None and int(stock) < 0:
            raise forms.ValidationError(
                format_html('<div class="alert alert-danger" role="alert">A simple danger alert—check it out!</div>')
            )

        if stock is None:
            raise forms.ValidationError('El campo stock no puede estar vacío.')
            
        stock = self.cleaned_data.get('stock')
        if stock is None:
            raise forms.ValidationError('El campo stock no puede estar vacío....')
        
        
        return stock

    