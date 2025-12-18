from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import ProductModel
from .serializers import ProductSerializer

class ProductListView(generics.ListAPIView):
    queryset = ProductModel.objects.filter(is_active=True)
    serializer_class = ProductSerializer

class ProductDetailsView(generics.RetrieveAPIView):
    queryset = ProductModel.objects.filter(is_active=True)
    serializer_class = ProductSerializer