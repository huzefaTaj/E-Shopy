from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customername=models.CharField(max_length=50, default='')
    city=models.CharField(max_length=100, default='')
    postcode=models.IntegerField(default='0')
    state=models.CharField(max_length=100, default='')
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    totalprice = models.IntegerField( default='0')
    status = models.BooleanField(default=False)
    orderid=models.CharField(max_length=500, default='', blank=True)
    paymentid=models.CharField(max_length=500, default='', blank=True)
    signatureid=models.CharField(max_length=500, default='', blank=True)
    
   

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

