from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from store.models.product import Product

def search( request):
    query=request.GET['query']
    products=Product.objects.filter(tag__icontains=query)
    params={'products':products}
    return render (request,'search.html',params)
    