from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from .serializers import OrdersSerializer
from .models import Orders


class OrderViewSet(viewsets.ModelViewSet):
    """
    订单视图
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrderCreateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    创建订单
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer