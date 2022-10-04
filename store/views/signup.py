from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):


    def get(self, request):
        return render(request, 'signup.html',{'nbar':'signupy'})

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        password2 = postData.get('password2')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        passw={'password2':password2}
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = self.validateCustomer(customer,passw)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            request.session.clear()
            request.session['vemail'] = first_name,last_name,email,phone, customer.password
            print("verify",  request.session['vemail'])
            customer.register()
            # return redirect('verify')
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value,
                'nbar':'signupy'
            }
            return render(request, 'signup.html', data)
         


    def validateCustomer(self, customer,passw):
        password2=passw['password2']
        # print(customer.password)
        error_message = None
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif customer.password != password2:
            error_message = ' Confirm Password Not Matched'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
