# Generated by Django 4.1.2 on 2023-06-23 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0005_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='productos'),
        ),
    ]
