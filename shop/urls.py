from django.urls import path
from .views import ProductsList, ProductsDetailList
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products-list', ProductViewSet, basename='products-list')

urlpatterns = [
    # path('products/', ProductsList.as_view({'get': 'list'}), name='products'),
    # path('products/<str:slug>/', ProductsList.as_view({'get': 'retrieve'}), name='product_detail')
    path('products/', ProductsList.as_view(), name='products'),
    path('products/<str:slug>/', ProductsDetailList.as_view(), name='product_detail')
]


urlpatterns += router.urls

