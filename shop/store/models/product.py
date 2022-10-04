from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=5001)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(default=None)
    image = models.ImageField(upload_to='uploads/products/',blank=True)
    image_url = models.CharField(max_length = 2083, blank=True)
    image_url2 = models.CharField(max_length = 2083, blank=True)
    image_url3 = models.CharField(max_length = 2083, blank=True)
    tag = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)


    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()