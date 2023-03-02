from rest_framework import serializers
from .models import Product, ProductCart


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price')


        


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    class Meta:
        model = ProductCart
        fields = '__all__'