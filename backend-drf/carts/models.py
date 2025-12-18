from django.db import models
from django.contrib.auth import get_user_model
from products.models import ProductModel
from decimal import Decimal

User = get_user_model()

# Create your models here.
class CartModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart({self.user})'
    
    @property # It let use to access this method as a field of cart model
    def subtotal(self):
        subtotal = Decimal('0.00')
        for item in self.items.all(): # here we use .items.all() because we set related_name='items' for cart in CarItemModel
            subtotal += item.product.price * item.quantity
        return subtotal
    
    @property
    def tax_amount(self):
        tax_amount = Decimal('0.00')
        for item in self.items.all():
            tax_amount += item.product.price * item.quantity * item.product.tax_percent / 100
        return tax_amount

    @property
    def grand_total(self):
        grand_total = self.subtotal + self.tax_amount
        return grand_total.quantize(Decimal('0.00'))

    
class CartItemModel(models.Model):  #related_name='items' lets you do:  cart.items.all()
    cart = models.ForeignKey(CartModel,on_delete=models.CASCADE, related_name='items') #ForeignKey is same like one to many / many to one 
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product.name} * {self.quantity}'
    
    @property
    def total_price(self):
        total_price = self.product.price * self.quantity
        return total_price