from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import CartModel, CartItemModel
from rest_framework.response import Response
from .serializers import CartSerializer,CartItemSerializer
from rest_framework import status
from products.models import ProductModel

# Create your views here.
class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        #get or create cart for loggedin user
        cart,created = CartModel.objects.get_or_create(user=request.user)
        serailizer = CartSerializer(cart)
        return Response(serailizer.data,status=status.HTTP_200_OK)
    
class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        if not product_id:
            return Response({'errors':'product_id is required'},status=status.HTTP_400_BAD_REQUEST)
        
        #get the product
        product = get_object_or_404(ProductModel,id=product_id,is_active=True)

        #get or create the cart
        cart, _ = CartModel.objects.get_or_create(user=request.user)

        #get or create cartitem
        item, created = CartItemModel.objects.get_or_create(cart=cart,product=product)

        if created:
            item.quantity = int(quantity)
        else:
            item.quantity += int(quantity) #just increase(add) quantity if item is already in cart

        item.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ManageCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request,item_id):
        #validate
        if 'delta' not in request.data: #delta(+1 or -1) is value which indicates whether to increase or decrease quantity
            return Response({"errors":"Provide delta field"},status=status.HTTP_400_BAD_REQUEST)
        
        delta = int(request.data.get('delta'))

        item = get_object_or_404(CartItemModel,id=item_id,cart__user=request.user) # __ used to access foregin key model(cart)'s fields

        product = item.product

        #for adding, check the stock
        if delta > 0: 
            if (item.quantity + delta) > product.stock:
                return Response({'error':'Not enough Stock'}) # return if there is no enough stock
            
        new_qty = item.quantity + delta #increase or decrease quantity

        if new_qty <= 0:
            #remove item from cart
            item.delete()
            return Response({'success':'Item Removed'})
        
        #save the new quantity
        item.quantity = new_qty
        item.save()
        serializer = CartItemSerializer(item)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,item_id):
        item = get_object_or_404(CartItemModel,id=item_id,cart__user=request.user) # __ used to access foregin key model(cart)'s fields
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)