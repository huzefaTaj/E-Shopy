from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from store.models.category import Category
from store.models.product import Product
from math import ceil









# def productview(request, myid):
  
    
    
    
#     product=Product.objects.filter(id=myid)

#     Category=Product.objects.values('category')


#     cats = {item['category'] for item in Category}
#     products=Product.get_all_products()
#     allProds = []
#     for cat in cats:
#         prod = Product.objects.filter(category=cat)
#         n = 3
#         nSlides = n // 4 + ceil((n / 4) - (n // 4))
#         allProds.append([prod, range(1, nSlides), nSlides])


#     params={'product':product[0], 'Category':Category,'products':products, 'allProds':allProds}
#     return render(request,'productview.html',params)

class productview(View):
    def post(self , request,myid):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])


        params={'product':product[0]}
        
        return  self.get( request,myid)


    def get(self, request,myid):

        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        print("view ",cart)
        product=Product.objects.filter(id=myid)
        Category=Product.objects.values('category')


        cats = {item['category'] for item in Category}
        products=Product.get_all_products()
        allProds = []
        for cat in cats:
            prod = Product.objects.filter(category=cat)
            n = 3
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            allProds.append([prod, range(1, nSlides), nSlides])


        params={'product':product[0], 'Category':Category,'products':products, 'allProds':allProds}
        return render(request,'productview.html',params)