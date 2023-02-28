from django.contrib import admin
from .models import Category, Product
from .forms import ProductAdminForm



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