from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string 
from django.contrib.auth.forms import UserCreationForm
from .models import Users
from .models import Cod
from .models import Card
# Create your views here.

def login(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def product(request):
    return render(request,'products.html')
def apparel(request):
    return render(request,'apparel.html')
def cart(request):
    return render(request,'cart.html')
def equip(request):
    return render(request,'equipments.html')
def kits(request):
    return render(request,'kits.html')
def supplement(request):
    return render(request,'supplements.html')
def sneakers(request):
    return render(request,'sneakers.html')
def account(request):
    return render(request,'account.html')
def login(request):
    return render(request,'login.html')
def access(request):
    return render(request,'accessories.html')


def account(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email=request.POST['email']
        Users(username=username,password=password,email=email).save()
        print()
        return render(request,'home.html')
    else:
        return render(request,'account.html')


def login(request):
    if request.method == 'POST':
        try:
            userDetails = Users.objects.get(username=request.POST['username'], password = request.POST['password'])
            request.session['username'] = userDetails.username
            print(userDetails.username)
            return render(request,'home.html',{'data':userDetails.username})
        except Exception as e:
            print(e,'invalid')
    return render(request,'login.html')


def cart(request):
    if request.method == 'POST':
        username = request.POST['username']
        address = request.POST['address']
        email=request.POST['email']
        state=request.POST['state']
        city=request.POST['city']
        pin=request.POST['pin']
        Cod(username=username,address=address,email=email,state=state,city=city,pin=pin).save()
        print()
        return render(request,'home.html')
    else:
        return render(request,'cart.html')

def cart(request):
    if request.method == 'POST':
        username = request.POST['username']
        address = request.POST['address']
        email=request.POST['email']
        state=request.POST['state']
        city=request.POST['city']
        pin=request.POST['pin']
        cardname=request.POST['cardname']
        cardnum=request.POST['cardnum']
        expmon=request.POST['expmon']
        expyr=request.POST['expyr']
        cvv=request.POST['cvv']
        Card(username=username,address=address,email=email,state=state,city=city,pin=pin,cardname=cardname,cardnum=cardnum,expmon=expmon,expyr=expyr,cvv=cvv).save()
        print()
        return render(request,'home.html')
    else:
        return render(request,'cart.html')


def logout(request):
    try:
        del request.session['username']
    except:
        return render(request,'home.html')
    return render(request,'login.html')
def success(request):
    email = EmailMessage('purchase ',
    'thanks',
    settings.EMAIL_HOST_USER,
    ['manigandan.241200@gmail.com'])

    email.fail_silently = False
    email.send()
    print("email send ")
    return render(request,'home.html')   


