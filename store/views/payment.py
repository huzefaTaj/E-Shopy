from django.shortcuts import render , redirect
import razorpay
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Product
from store.models.orders import Order
keyid='rzp_test_hirfh6v5D2YqkU'
keysecret='WgCujVIUZrJBnsZyelFKAnp2'


class Payment(View):
    def get(self,request):
        customer_id=Customer.get_customer_by_email(request.session['email']).id
        customer_email=str(Customer.get_customer_by_email(request.session['email']))
        try:
            order = request.session['order']
            customername = order['customername']
            city = order['city']
            address = order['address']
            postcode = order['postcode']
            state = order['state']
            phone = order['phone']
            cart = request.session.get('cart')
            products = Product.get_products_by_id(list(cart.keys()))

            totalprice = int(request.session['TotalPrice'])
            client = razorpay.Client(auth=(keyid, keysecret))
            data = {
                'amount': totalprice * 100,
                'currency': "INR",
                'receipt': "hello123",
                "notes": {
                    "Customer Id": customer_id,
                    "email:": customer_email,
                    "Name:": customername,
                    "PhoneNo.:": phone,
                    "Address:": address,
                    "State:": state,
                    "City": city

                }
            }
            order = client.order.create(data=data)
            order_id = order['id']
            all = {'orderid': order_id, 'totalprice': totalprice, 'customername': customername, 'address': address,
                   'postcode': postcode, 'phone': phone, 'customer_email': customer_email, 'products': products}
            return render(request, 'payment.html', all)
        except:
            return  redirect('homepage')

    def post(self,request):

        order = request.session['order']
        print('order', order)
        customername = order['customername']
        city = order['city']
        address = order['address']
        postcode = order['postcode']
        state = order['state']
        phone = order['phone']
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        razorpay_payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        razorpay_signature = request.POST.get('razorpay_signature', '')

        for product in products:
            orderr = Order(customer=Customer(id=customer),
                           customername=customername,
                           city=city,
                           postcode=postcode,
                           state=state,
                           product=product,
                           price=product.price,
                           address=address,
                           phone=phone,
                           quantity=cart.get(str(product.id)),
                           totalprice=product.price * cart.get(str(product.id)),
                           orderid =razorpay_order_id,
                           paymentid =razorpay_payment_id,
                           signatureid=razorpay_signature)

            client = razorpay.Client(auth=(keyid, keysecret))
            razorpay_payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            razorpay_signature = request.POST.get('razorpay_signature', '')

            payment_id = {'razorpay_payment_id': razorpay_payment_id,
                         'razorpay_order_id': razorpay_order_id,
                         'razorpay_signature': razorpay_signature}
            try:
                verify = client.utility.verify_payment_signature(payment_id)
                print("verify",verify)
                print("payment done")
                orderr.save()
            except:
                print("error")
        request.session['cart'] = {}
        request.session['TotalPrice']={}
        request.session['order']={}
        return redirect('thankyou')