# Generated by Django 4.2.5 on 2023-09-13 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cart", "0003_rename_product_name_product_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("content", models.TextField()),
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