from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from techlaps_stock.auth import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework.decorators import action
from django.views import generic


class BookListView(generic.ListView):
    model = Order
    context_object_name = 'orders'   # your own name for the list as a template variable
    template_name = 'product_list.html'  # Specify your own template name/location

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['test'] = 123
        return context


class ProductViewSet(viewsets.ViewSet):
    # permission_classes = IsAuthenticated

    def list(self, request):
        queryset = Product.objects.all()

        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk, format=None):
        snippet = Product.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk=None):

        job = Product.objects.get(pk=pk)
        serializer = ProductSerializer(job, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    @action(methods=['post'], detail=False,)
    def get_cart(self, request, pk=None, *args, **kwargs):
        print(request.data)

        Order.objects.create(
            user=User.objects.get(pk=request.data["user"]), content=request.data["order"])
        print(request.data)
        return Response(request.data)
