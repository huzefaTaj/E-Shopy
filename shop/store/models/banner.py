from django.db import models
from .category import Category

class Banner(models.Model):
    carousel_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="shop/images", default="")
    category= models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True, default=1)

    @staticmethod
    def get_all_Banner():
        return Banner.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid2(category_id):
        if category_id:
            return Banner.objects.filter(category = category_id )
        else:
            return Banner.objects.all()
