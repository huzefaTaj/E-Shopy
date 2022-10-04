from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.customer import Customer
from django.views import View
from django.contrib import messages
import  random
import smtplib

class verify(View):
    def get(self, request):


        cotp = random.randrange(100000, 1000000)
        print('veify',cotp)
        dotp=cotp
        cotp=make_password(str(cotp))
        print(cotp)
        email=request.session['vemail']
        verifyemail=email[2]

        phone = request.session['vemail']

        first_name = request.session['vemail']

        last_name= request.session['vemail']

        password = request.session['vemail']

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("tajhuzefa91@gmail.com", "write password here ")
        Subject = "OTP"
        text = """\
               Hi,
               Verify Your Account :
               """ + str(dotp) + """ """
        message = 'Subject: {}\n\n{}'.format(Subject, text)

        s.sendmail("tajhuzefa91@gmail.com", str(verifyemail), message)
        print(verifyemail)
        s.quit()

        data={'cotp':cotp,'email':email[2],'phone':phone[3],'first_name':first_name[0],'last_name':last_name[1],'password':password[4]}
        return render(request, 'verifyemail.html', data )

    def post(self,request):

        first_name = request.POST.get('first_name','')
        last_name = request.POST.get('last_name','')
        email = request.POST.get('email','')
        print("post", email)
        phone = request.POST.get('phone','')
        password = request.POST.get('password','')
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)


        cotp =request.POST.get('cotp')
        print('encrypted',cotp)
        otp = request.POST.get('otp')
        print (otp)
        flag = check_password(otp, cotp)
        if flag:

            customer.register()
            request.session.clear()
            return redirect('homepage')
        else:
            messages.info(request, "OTP is not Correct")
            messages.info(request, " New OTP Sent ")
            return self.get(request)


