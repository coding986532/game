from turtle import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.URLField()
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Transaction(models.Model):
    Property = models.ForeignKey(Listing, on_delete=models.CASCADE)
    Buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    Method = models.CharField(max_length=100)
    price = models.IntegerField()
    Complete = models.BooleanField()