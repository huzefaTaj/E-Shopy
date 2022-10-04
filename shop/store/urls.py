from django.contrib import admin
from django.urls import path
from .views.home import Index ,store
from .views.search import search
from .views.productview import productview
from .views.signup import Signup
from .views.verify import verify
from .views.cart import Cart
from .views.login import Login , logout
from .views.orders import OrderView
from .views.checkout import CheckOut
from .views.payment import Payment
from .views.thankyou import Thankyou
from .middlewares.auth import  auth_middleware

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('productview/<int:myid>', productview.as_view() , name='productview/<int:myid>'),
    path('search', search , name='search'),
    path('signup', Signup.as_view(), name='signup'),
    path('verify', verify.as_view(), name='verify'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', Cart.as_view() , name='cart'),
    path('orders', auth_middleware( OrderView.as_view()), name='orders'),
    path('check-out',auth_middleware( CheckOut.as_view()) , name='checkout'),
    path('payment', Payment.as_view(), name='payment'),
    path('thankyou', Thankyou.as_view(), name='thankyou')

]
