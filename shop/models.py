from django.db import models



class Category(models.Model):
    name = models.CharField('Название категории', max_length=50)
    slug = models.SlugField('url',)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField('Наименование товара', max_length=255)
    slug = models.SlugField('url', )
    description = models.TextField('Описание продукта',)
    price = models.DecimalField(max_digits=999, decimal_places=2)
    game = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.name
