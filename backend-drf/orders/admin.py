from django.contrib import admin
from .models import OrderItem,OrderModel


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['order','product','quantity','price','total_price']

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

# Register your models here.
admin.site.register(OrderModel,OrderAdmin)  #it makes the order items display inside order page instead of seperate page for order items
# admin.site.register(OrderItem)