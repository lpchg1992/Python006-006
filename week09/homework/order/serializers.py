from rest_framework import serializers
from .models import Orders


class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'title', 'details']