from rest_framework import serializers
from .models import Product


class ProductsListSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Product
        fields = ('name', 'price', 'url')


        


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'