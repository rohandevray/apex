# Generated by Django 4.2.5 on 2023-09-12 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_product_cart_items_cart_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
