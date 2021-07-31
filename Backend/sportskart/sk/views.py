from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from .models import Users
from .models import Cash
from .models import Card
from .models import Home,Sneak,Access,Apparel,Supp,Kits,Equip
import random
# Create your views here.

def login(request):
    return render(request,'index.html')
def home(request):
    prod = Home.objects.all()
    return render(request,'home.html',{'prod':prod})
def product(request):
    return render(request,'products.html')
def apparel(request):
    prod = Apparel.objects.all()
    return render(request,'apparel.html',{'prod':prod})
def cart(request):
    return render(request,'cart.html')
def card(request):
    return render(request,'card.html')
def cash(request):
    return render(request,'cash.html')
def confirm(request):
    return render(request,'confirm.html')
def equip(request):
    prod = Equip.objects.all()
    return render(request,'equipments.html',{'prod':prod})
def kits(request):
    prod = Kits.objects.all()
    return render(request,'kits.html',{'prod':prod})
def supplement(request):
    prod = Supp.objects.all()
    return render(request,'supplements.html',{'prod':prod})
def sneakers(request):
    prod = Sneak.objects.all()
    return render(request,'sneakers.html',{'prod':prod})
def account(request):
    return render(request,'account.html')
def login(request):
    return render(request,'login.html')
def access(request):
    prod = Access.objects.all()
    return render(request,'accessories.html',{'prod':prod})
def abt(request):
    return render(request,'about.html')

def account(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email=request.POST['email']

        if Users.objects.filter(username=username).exists():
            messages.info(request,"Username Taken")
            return redirect('account')
        elif Users.objects.filter(email=email).exists():
            messages.info(request,"Email Taken")
            return redirect('account')
        else:
            Users(username=username,password=password,email=email).save()
            prod = Home.objects.all()
            return render(request,'home.html',{'data':username,'prod':prod})
    else:
        return render(request,'account.html')


def login(request):
    if request.method == 'POST':
        try:
            userDetails = Users.objects.get(username=request.POST['username'], password = request.POST['password'])
            request.session['username'] = userDetails.username
            print(userDetails.username)
            prod = Home.objects.all()
            return render(request,'home.html',{'data':userDetails.username,'prod':prod})
        except Exception as e:
            print(e,'invalid')
    return render(request,'login.html')


def cash(request):
    if request.method == 'POST':
        username = request.POST['username']
        address = request.POST['address']
        email=request.POST['email']
        state=request.POST['state']
        city=request.POST['city']
        pin=request.POST['pin']
        Cash(username=username,address=address,email=email,state=state,city=city,pin=pin).save()
        print()
        num=random.randint(1000000000,9999999999)
        template=render_to_string('sk/email_template.html',{'name':username,'num':num})
        email = EmailMessage('SportsKart-Confirmation',
        template,
        settings.EMAIL_HOST_USER,
        [email,'manirockzz.2000@gmail.com'])
        email.fail_silently = False
        email.send()
        return render(request,'home.html',{'data':username})
    else:
        return render(request,'cash.html')

def card(request):
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
        num=random.randint(1000000000,9999999999)
        template=render_to_string('sk/email_template.html',{'name':username,'num':num})
        email = EmailMessage('SportsKart-Confirmation',
        template,
        settings.EMAIL_HOST_USER,
        [email,'manirockzz.2000@gmail.com'])
        email.fail_silently = False
        email.send()
        return render(request,'home.html',{'data':username})
    else:
        return render(request,'card.html')

# def home(request):
#     prod = Home.objects.all()

#     return render(request,"home.html",{'prod':prod})


