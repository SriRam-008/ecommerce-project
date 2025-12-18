from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from carts.models import CartItemModel,CartModel
from rest_framework.response import Response
from .models import OrderItem,OrderModel
from .serializers import OrderSerializer
from rest_framework import status
from .utils import send_order_notification
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Create your views here.
class PlaceOrderView(APIView):
    #user must loggedin
    permission_classes = [IsAuthenticated]

    def post(self,request):
        cart = CartModel.objects.get(user=request.user)
        #check cart is not empty
        if not cart or cart.items.count() == 0:
            return Response({'error':'Cart is empty'},status=status.HTTP_400_BAD_REQUEST)
        
        #create the order
        order = OrderModel.objects.create(
            user=request.user,
            sub_total=cart.subtotal,
            tax_amount=cart.tax_amount,
            grand_total = cart.grand_total
        )

        #create order items ,in this each cart_item become order_item
        for item in cart.items.all():
            OrderItem.objects.create(
                order = order,
                product = item.product,
                quantity = item.quantity,
                price = item.product.price,
                total_price = item.total_price
            )

        #clear the cart items
        cart.items.all().delete()

        #send notification email
        send_order_notification(order)

        #send response to frontend
        serializer = OrderSerializer(order)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    

class OrdersView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self): #Overwriting queryset
        return OrderModel.objects.filter(user=self.request.user)
    
class OrderDetailsView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()