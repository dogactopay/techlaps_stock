from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    created = models.DateTimeField(auto_now_add=True)

    id = models.AutoField(primary_key=True)
    sku = models.IntegerField(default=0)

    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    stock_qty = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['created']


class Order(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,

    )
    id = models.AutoField(primary_key=True)

    content = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['created']