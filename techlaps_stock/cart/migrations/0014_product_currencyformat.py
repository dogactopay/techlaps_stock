# Generated by Django 4.2.6 on 2023-10-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0013_product_desi"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="currencyFormat",
            field=models.CharField(blank=True, default="$", max_length=5),
        ),
    ]
