from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout
from .models import Products,Customer,Order,OrderUpdate
from . import forms
from django.contrib.auth.models import User,auth
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from . import Checksum
from django.views.decorators.csrf import csrf_exempt
MERCHANT_KEY = 'A&axvn2njyg0Nc&c'


# Create your views here.
def index(request):
    products = Products.objects.all().order_by('id')[:9]
    return render(request,'products/index.html',{'Products':products})


def about(request):
    products = Products.objects.all().order_by('id')[:9]
    return render(request,'products/about.html',{'Products':products})


def contact(request):
    products = Products.objects.all().order_by('id')[:9]
    return render(request,'products/contact.html',{'Products':products})


def products(request):
    products = Products.objects.all().order_by('id')
    return render(request,'products/product.html',{'Products':products})


def cartinsert(request):
        return render(request,'products/addressform.html')
    
def cartPayment(request):
    cart = Cart(request)
    if request.method == "POST":
        for key in cart.cart:
            print(key)
            address = request.POST["address"]
            pincode = request.POST["pincode"]
            cartitems = cart.cart[key]
            product=cartitems["product_id"]
            userid=cartitems["userid"]
            productprice = int(cartitems["price"])
            #print(productprice)
            price = int(int(cartitems["price"])*int(cartitems["quantity"]))
            totprice = price
            obj_id = get_object_or_404(Products, id=product)
            objuser_id = get_object_or_404(Customer, id=userid)
            order = Order.objects.create(product_id=obj_id,user_id=objuser_id,
                                         price=productprice,total=totprice,address=address,phonenumber=pincode)
            update = OrderUpdate(order_id=order.id, update_desc="The order has been placed")
            update.save()
            thank = True
            id = order.id
            # Request paytm to transfer the amount to your account after payment by user
            param_dict = {
                    'MID': 'RJxELd53016280222487',
                    'ORDER_ID': str(order.id),
                    'TXN_AMOUNT': '1',
                    'CUST_ID': 'narenderp143112@gmail.com',
                    'INDUSTRY_TYPE_ID': 'Retail',
                    'WEBSITE': 'WEBSTAGING',
                    'CHANNEL_ID': 'WEB',
                    'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict,MERCHANT_KEY)
            return render(request, 'products/paytm.html', {'param_dict': param_dict})
        # order.save();
    
@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    checksum=''
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            error_message ="order successful"
        else:
            error_message ='order was not successful because' + response_dict['RESPMSG']
    return render(request, 'products/paymentstatus.html', {'response': response_dict,'error':error_message})



def login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        #user = Customer.objects.get(email=email)
        user = get_object_or_404(Customer,email=email)
        error_message = None
        if user is not None:
            # auth.login(request,user)
            flag=check_password(password,user.password)
            if flag:
                request.session['id']=user.id
                request.session['email']=user.email
                request.session['username']=user.username
                return redirect('/')
            else:
                error_message ="Password is Incorrect"
        else:
            error_message ="Email Doesn't Exist"
        return render(request,'products/login.html',{'error':error_message})
    else:
        # if request.session.get('id')!='':
        #     return redirect('/')
        # else:
        return render(request,'products/login.html')
    # else:
    #     return redirect('/')
    
def logout(request):
    request.session.clear()
    cart = Cart(request)
    cart.clear()
    return redirect('/')

def profile(request):
    id = request.session['id']
    user = get_object_or_404(Customer,id=id)
    order = get_object_or_404(Order,user_id=id)
    print(order)
    return render(request,'products/profile.html',{'user':user,});


def register(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password1 = request.POST['password1']
        error_message=validateCustomer(first_name,last_name,username,email,phone,password,password1)
        if not error_message:
                password=make_password(password)
                user = Customer.objects.create(first_name=first_name,last_name=last_name,username=username,email=email,
                                            password=password,phone=phone)
                user.save()
                return redirect('/accounts/register') 
        else:
            return render(request,'products/register.html',{'error':error_message})
            # return redirect(accountregister,error=error_message)  
    else:
        return render(request,'products/register.html')
    
def accountregister(request,error):
    return render(request,'products/register.html',{'error':error})
      
    

def checkout(request):
    if request.session.has_key('username'):
        return render(request,'products/checkout.html')
    else:
        return render(request,'products/login.html')
    # else:
    #     redirect('/accounts/login')
        




def viewdetails(request,id):
    obj=Products.objects.get(id=id)
    return render(request,'products/viewdetails.html',{'details':obj})





def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")



def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")



def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")



def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")



def cart_detail(request):
    return render(request, 'products/cart_detail.html')



def validateCustomer(first_name,last_name,username,email,phone,password,password1):
    error_message = None
    if(not first_name):
        error_message = "First Name Required !!!"
    elif len(first_name)< 4:
        error_message = 'First name character should be more than 4'  
    elif not last_name:
        error_message = "Last Name Required !!!"
    elif len(last_name)<4:
        error_message = "Last Name character should be more than 4"
    elif not username:
        error_message = "Username is Required!!"
    elif len(username)<4:
        error_message = "Username Character should be more than 4"
    elif not email:
        error_message = "Email is Required!!"
    elif not phone:
        error_message = "Phone is Required!!"
    # elif len(phone)<=11:
    #     error_message = "Phone Character should be more than 12"
    elif not password:
        error_message = "password is Required!!"
    elif len(password)<6:
        error_message = "password Character should be more than 6"
    elif not password1:
        error_message = "Confirm password is Required!!"
    elif len(password1)<6:
        error_message = "Confirm password Character should be more than 6"
    elif password!=password1:
        error_message = "Confirm password and Password should be Same"
    elif Customer.objects.filter(username=username).exists():
        error_message = "Username Already Exist"
    elif Customer.objects.filter(email=email).exists():
        error_message = "Email Already Exist"
    return error_message
    





    
    
    
    
