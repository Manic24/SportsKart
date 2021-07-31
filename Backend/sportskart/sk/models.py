from django.db import models
from django.db.models.fields import IntegerField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.
class Users (models.Model):
    username=models.CharField(blank=True,max_length=100)
    email=models.EmailField(blank=False,max_length=100)
    password=models.CharField(blank=True,max_length=100)

    def __str__(self):
        return self.username
class Home(models.Model):
    prodname=models.CharField(blank=False,max_length=50)
    img=models.ImageField(upload_to='images')
    price=models.IntegerField(blank=False)
    addcart=models.CharField(blank=False,max_length=20)

    def __str__(self):
        return self.prodname
class Apparel(models.Model):
    prodname=models.CharField(blank=False,max_length=50)
    img=models.ImageField(upload_to='images')
    price=models.IntegerField(blank=False)
    addcart=models.CharField(blank=False,max_length=20)

    def __str__(self):
        return self.prodname
class Access(models.Model):
    prodname=models.CharField(blank=False,max_length=50)
    img=models.ImageField(upload_to='images')
    price=models.IntegerField(blank=False)
    addcart=models.CharField(blank=False,max_length=20)

    def __str__(self):
        return self.prodname
class Equip(models.Model):
    prodname=models.CharField(blank=False,max_length=50)
    img=models.ImageField(upload_to='images')
    price=models.IntegerField(blank=False)
    addcart=models.CharField(blank=False,max_length=20)

    def __str__(self):
        return self.prodname
class Kits(models.Model):
    prodname=models.CharField(blank=False,max_length=50)
    img=models.ImageField(upload_to='images')
    price=models.IntegerField(blank=False)
    addcart=models.CharField(blank=False,max_length=20)

    def __str__(self):
        return self.prodname
class Supp(models.Model):
    prodname=models.CharField(blank=False,max_length=50)
    img=models.ImageField(upload_to='images')
    price=models.IntegerField(blank=False)
    addcart=models.CharField(blank=False,max_length=20)

    def __str__(self):
        return self.prodname
class Sneak(models.Model):
    prodname=models.CharField(blank=False,max_length=50)
    img=models.ImageField(upload_to='images')
    price=models.IntegerField(blank=False)
    addcart=models.CharField(blank=False,max_length=20)

    def __str__(self):
        return self.prodname

class Cash(models.Model):
    username=models.CharField(blank=False,max_length=20)
    email=models.EmailField(blank=False,max_length=50)
    address=models.CharField(blank=False,max_length=50)
    city=models.CharField(blank=False,max_length=20)
    state=models.CharField(blank=False,max_length=20)
    pin=models.IntegerField(blank=False)

    def __str__(self):
        return self.username

class Card(models.Model):
    
    username=models.CharField(blank=False,max_length=20)
    email=models.EmailField(blank=False,max_length=50)
    address=models.CharField(blank=False,max_length=50)
    city=models.CharField(blank=False,max_length=20)
    state=models.CharField(blank=False,max_length=20)
    pin=models.IntegerField(blank=False)
    cardname=models.CharField(blank=False,max_length=20)
    cardnum=models.IntegerField(blank=False)
    expmon=models.CharField(blank=False,max_length=20)
    expyr=models.CharField(blank=False,max_length=4)
    cvv=models.IntegerField(blank=False)

    def __str__(self):
        return self.username