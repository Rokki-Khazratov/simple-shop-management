# Generated by Django 5.0.2 on 2024-03-22 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debtors',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, to='product.product'),
        ),
    ]
