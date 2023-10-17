from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = "__all__"



class OrderSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username"
    )

    class Meta:
        model = Order

        fields = ['id', 'created', 'content',
                  "username", "status"]


class OrderChangeSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username"
    )

    class Meta:
        model = Order

        fields = "__all__"
