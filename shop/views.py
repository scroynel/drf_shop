from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductsListSerializer, ProductDetailSerializer
from rest_framework.response import Response

class ProductsList(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductsListSerializer(queryset, many=True,)
        return Response(serializer.data)
    
    def retrieve(self, request, slug):
        product = Product.objects.get(slug=slug)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
