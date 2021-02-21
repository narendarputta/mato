from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime


# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    preview = models.IntegerField()
    description = models.TextField()
    image = models.ImageField()
    
    
class Customer(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=100)
    password=models.CharField(max_length=100)
      
    
     
class Order(models.Model):
    product_id = models.ForeignKey(Products, related_name='products', on_delete=models.CASCADE)
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE,default="")
    address = models.TextField()
    phonenumber=models.CharField(max_length=100)
    price = models.FloatField()
    total = models.FloatField()
    timestamp = models.DateTimeField(default=datetime.datetime.today)

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

    
