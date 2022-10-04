from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        try:
           customer = Customer.get_customer_by_email(request.session['email'])
           customerphone=customer.phone
           customer_First_name=customer.first_name
           customer_Last_name= customer.last_name
           customer_Full_name =customer_First_name+" "+customer_Last_name
           data={'products' : products, 'customerphone':customerphone ,'customer_Full_name':customer_Full_name,'nbar': 'carty'}
           return render(request , 'cart.html' , data )
        except:
             data={'products' : products,'nbar': 'carty'}
             return render(request , 'cart.html' , data )

        
       

