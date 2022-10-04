from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from store.models.banner import Banner
class Carousel(View):
    def get(self, request):
        carousel=Carousel.get_all_Banner()
        print(carousel)
        return redirect(request,'homepage',{'carousel':carousel})
