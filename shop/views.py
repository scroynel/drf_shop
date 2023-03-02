from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from .models import Product, ProductCart
from .serializers import ProductsListSerializer, ProductDetailSerializer, CartSerializer
from rest_framework.response import Response
from rest_framework import permissions

# -------- ViewSet

# class ProductsList(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Product.objects.all()
#         serializer = ProductsListSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, slug):
#         product = Product.objects.get(slug=slug)
#         serializer = ProductDetailSerializer(product)
#         return Response(serializer.data)


# -------- APIView

# class ProductsList(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductsListSerializer(products, many=True)
#         return Response(serializer.data)
    
# class ProductDetailList(APIView):
#     def get(self, request, slug):
#         product = Product.objects.get(slug=slug)
#         serializer = ProductDetailSerializer(product)
#         return Response(serializer.data)


# -------- generics

# class ProductsList(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductsListSerializer


# class ProductsDetailList(generics.RetrieveAPIView):
#     lookup_field = 'slug'
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailSerializer


# -------- ReadOnlyModelViewSet (list, retrieve)

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

class CartProducts(viewsets.ViewSet):
    def list(self, request):
        queryset = ProductCart.objects.all()
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)
    
