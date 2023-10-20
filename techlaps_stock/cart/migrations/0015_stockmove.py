# Generated by Django 4.2.6 on 2023-10-20 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cart", "0014_product_currencyformat"),
    ]

    operations = [
        migrations.CreateModel(
            name="StockMove",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("move", models.CharField(blank=True, max_length=500)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cart.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["created"],
            },
        ),
    ]