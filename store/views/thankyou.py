from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
class Thankyou(View):
    def get(self, request):
        return render(request, 'thankyou.html')
