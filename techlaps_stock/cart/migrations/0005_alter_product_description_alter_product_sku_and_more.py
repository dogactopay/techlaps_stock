# Generated by Django 4.2.6 on 2023-10-16 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0004_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name="product",
            name="sku",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
