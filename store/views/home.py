from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from store.models.banner import Banner
from store.models.category import Category
from store.models.product import Product
from math import ceil
class Index(View):

    def get(self , request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}',{'nbar': 'homee'})

   

  



def store(request):

    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    
    carousel=Banner.get_all_Banner()
    
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['carousel'] = carousel
    data['products'] = products
    data['categories'] = categories
    data['nbar'] = 'homee'

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)

