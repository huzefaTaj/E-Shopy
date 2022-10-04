from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
class CheckOut(View):

    def post(self, request):
        address = request.POST.get('address')
        customername=request.POST.get('customername')
        city=request.POST.get('city')
        postcode=request.POST.get('postcode')
        state=request.POST.get('state')
        totalproduct = request.POST.get('totalproduct')
        # request.session['TotalPrice'] =totalproduct
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)
        total=[]
        for product in products:
             print(cart.get(str(product.id)))
             order = Order(customer=Customer(id=customer),
                          customername=customername,
                          city=city,
                          postcode=postcode,
                          state=state,
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)),
                          totalprice =product.price * cart.get(str(product.id)) )
             total.append(order.totalprice)
             if customer == customer:
                 if len(phone) < 10:
                    messages.info(request,"phone number is not correct")
                    return redirect('cart')
                 elif   len(address) == 0:
                     messages.info(request,"Address Field  is empty")
                     return redirect('cart') 
                 elif   len(city) == 0: 
                     messages.info(request,"city Field  is empty")
                     return redirect('cart')   
                 elif   len(postcode) == 0:   
                     messages.info(request,"postcode Field  is empty")
                     return redirect('cart') 
                 elif   len(state) == 0:   
                     messages.info(request,"state Field  is not correct")
                     return redirect('cart')   
                 else:
                     dataa={'customername':order.customername,
                            'city':order.city,
                            'postcode':order.postcode,
                            'state':order.state,
                            'address':order.address,
                            'phone':order.phone,
                            }
                     request.session['order'] = dataa

                     # order.save()
                     # request.session['cart'] = {}

        totalp= sum(total)
        request.session['TotalPrice'] = totalp
        return redirect('payment')
