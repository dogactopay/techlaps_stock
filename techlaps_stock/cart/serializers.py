from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import serializers
from .models import *



class ProductSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = Product

        fields = "__all__"
