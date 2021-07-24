from django.db import models

# Create your models here.
class Users (models.Model):
    username=models.CharField(blank=True,max_length=100)
    email=models.EmailField(blank=False,max_length=100)
    password=models.CharField(blank=True,max_length=100)

    def __str__(self):
        return self.username

class Cod(models.Model):
    username=models.CharField(blank=False,max_length=20)
    email=models.EmailField(blank=False,max_length=30)
    address=models.CharField(blank=False,max_length=50)
    city=models.CharField(blank=False,max_length=10)
    state=models.CharField(blank=False,max_length=10)
    pin=models.IntegerField(blank=False)

    def __str__(self):
        return self.username

class Card(models.Model):
    
    username=models.CharField(blank=False,max_length=20)
    email=models.EmailField(blank=False,max_length=30)
    address=models.CharField(blank=False,max_length=50)
    city=models.CharField(blank=False,max_length=10)
    state=models.CharField(blank=False,max_length=10)
    pin=models.IntegerField(blank=False)
    cardname=models.CharField(blank=False,max_length=20)
    cardnum=models.IntegerField(blank=False)
    expmon=models.CharField(blank=False,max_length=10)
    expyr=models.CharField(blank=False,max_length=4)
    cvv=models.IntegerField(blank=False)

    def __str__(self):
        return self.username