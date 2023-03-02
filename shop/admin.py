from django.contrib import admin
from .models import Category, Product, Customer, Cart, ProductCart
from .forms import ProductAdminForm

admin.site.register(Customer)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ('name',),}

admin.site.register(Category, CategoryAdmin)

class ProductyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price']
    list_display_links = ['id', 'name']
    form = ProductAdminForm
    prepopulated_fields = {'slug': ('name',),}
    

admin.site.register(Product, ProductyAdmin)
admin.site.register(Cart)
admin.site.register(ProductCart)
