from django.urls import path
from .views import ProductsList

urlpatterns = [
    path('products/', ProductsList.as_view({'get': 'list'}), name='products'),
    path('products/<str:slug>/', ProductsList.as_view({'get': 'retrieve'}), name='product_detail')
]