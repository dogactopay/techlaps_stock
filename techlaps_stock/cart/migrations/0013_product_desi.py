# Generated by Django 4.2.6 on 2023-10-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0012_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="desi",
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
