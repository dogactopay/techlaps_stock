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
from django.contrib.auth.models import User


class OrderViewSet(viewsets.ViewSet):
    # permission_classes = IsAuthenticated

    def list(self, request):
        user_id = request.user.id
        if user_id:
            query = User.objects.filter(id=user_id).values_list(
                "is_staff", flat=True)[0]

            print(query)
            if query:
                queryset = Order.objects.all().order_by('status', '-created')
            else:
                queryset = Order.objects.filter(
                    user=user_id).order_by('status', '-created')
        else:
            queryset = Order.objects.all().order_by('status', '-created')
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk, format=None):
        snippet = Order.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk=None):

        old_st = Order.objects.filter(id=request.data['id']).values_list(
            "status", flat=True)[0]

        if old_st != 1 and request.data['status'] == 1:
            for p in request.data['content']:
                stck = Product.objects.filter(id=p['id']).values_list(
                    "stock_qty", flat=True)[0]
                Product.objects.filter(id=p['id']).update(
                    stock_qty=stck-p['quantity'])

                StockMove.objects.create(user=User.objects.get(
                    pk=1), product=Product.objects.get(pk=p['id']), move=f"-{p['quantity']}")

        job = Order.objects.get(pk=pk)
        print(request.data)
        serializer = OrderChangeSerializer(job, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(request.data)


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

        StockMove.objects.create(
            user=User.objects.get(pk=1), product=Product.objects.get(pk=serializer.data['id']), move=f"+{serializer.data['stock_qty']}")

        return Response(serializer.data)

    def destroy(self, request, pk, format=None):
        snippet = Product.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk=None):

        job = Product.objects.get(pk=pk)

        diff = int(request.data['stock_qty']) - \
            list(Product.objects.filter(id=pk).values_list(
                "stock_qty", flat=True))[0]

        print(int(request.data['stock_qty']))
        print(diff)
        if "-" in str(diff):
            move1 = diff
        else:
            move1 = f"+{diff}"
        StockMove.objects.create(
            user=User.objects.get(pk=1), product=Product.objects.get(pk=pk), move=move1)

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


class StockMoveViewSet(viewsets.ViewSet):
    # permission_classes = IsAuthenticated

    def list(self, request):
        queryset = StockMove.objects.all()

        serializer = StockMoveSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = StockMoveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk, format=None):
        snippet = StockMove.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk=None):

        job = StockMove.objects.get(pk=pk)
        serializer = StockMoveSerializer(job, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
