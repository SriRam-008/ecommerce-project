from rest_framework import serializers
from .models import CartModel, CartItemModel

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name',read_only=True) #accessing forign key fileds, its like colning that field
    price  = serializers.DecimalField(max_digits=10,decimal_places=2,source='product.price',read_only=True)
    tax_percent = serializers.DecimalField(max_digits=10,decimal_places=2,source='product.tax_percent',read_only=True)
    class Meta:
        model = CartItemModel
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    subtotal = serializers.DecimalField(max_digits=10,decimal_places=2) #value will come from Cart Model (method we create)
    tax_amount = serializers.DecimalField(max_digits=10,decimal_places=2)
    grand_total = serializers.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
        model = CartModel
        fields = '__all__'
    
