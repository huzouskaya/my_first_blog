# Generated by Django 5.1.3 on 2024-11-17 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_alter_products_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.CharField(blank=True, max_length=400, null=True, unique=True, verbose_name='URL изображения'),
        ),
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Размер'),
        ),
    ]