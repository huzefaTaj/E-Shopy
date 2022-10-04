from django.contrib import admin
from .models.category import Category
from .models.product import Product
from .models.customer import Customer
from .models.orders import Order
from .models.banner import Banner

# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','image', 'price', 'category']

class AdminOrder(admin.ModelAdmin):
    list_display = ['customer', 'customername','address','city','postcode','product', 'quantity','orderid','paymentid', 'totalprice','date','status']

class AdminBanner(admin.ModelAdmin):
    list_display = ['carousel_id']

admin.site.register(Category , AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Banner, AdminBanner)
admin.site.register(Customer)
admin.site.register(Order,AdminOrder )
