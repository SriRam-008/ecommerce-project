from rest_framework import serializers
from .models import OrderItem,OrderModel

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    # items = OrderItemSerializer(many=True, read_only=True)  
    class Meta:
        model = OrderModel
        fields = '__all__'


