from turtle import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

property_type_choices = (
    ('House', 'House'),
    ('Apartment Complex', 'Apartment Complex'),
    ('Apartment Unit', 'Apartment Unit'),
    ('Condo', 'Condo'),
    ('Building', 'Building'),
    ('Land', 'Land'),
    ('Business', 'Business'),
    ('Business Suite', 'Business Suite'),
    ('Shop', 'Shop'),
    ('Warehouse', 'Warehouse'),
    ('Storage', 'Storage'),
    ('Office', 'Office'),
    ('Other', 'Other'), 

) 
class Listing(models.Model):
    name = models.CharField(max_length=100)
    property_type = models.CharField(max_length=500, choices=property_type_choices)
    street = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100)
    territory = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.URLField()
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Transaction(models.Model):
    Property = models.ForeignKey(Listing, on_delete=models.CASCADE)
    Buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    Method = models.CharField(max_length=100)
    price = models.IntegerField()
    Complete = models.BooleanField()