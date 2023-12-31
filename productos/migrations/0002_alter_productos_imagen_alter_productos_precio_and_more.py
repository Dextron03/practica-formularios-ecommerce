# Generated by Django 5.0 on 2023-12-29 14:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='img_productos'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, error_messages={'min_value': '<div class="alert alert-danger" role="alert"> Ingrese un valor mayor o igual a cero. </div>'}, help_text='El precio del producto.', max_digits=8, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='productos',
            name='stock',
            field=models.PositiveBigIntegerField(blank=True, default=0, error_messages={'min_value': '<div class="alert alert-danger" role="alert">A simple danger alert—check it out!</div>'}, help_text='Cantidad que tiene disponible', validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
