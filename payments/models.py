
from django.db import models
from django.urls import reverse
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
    name = models.CharField(max_length=100, help_text="Name of the property, street specifically, again.")
    property_type = models.CharField(max_length=500, choices=property_type_choices)
    square_feet = models.CharField(max_length=100, blank=True)
    lot_size = models.CharField(max_length=100, blank=True)
    stories = models.CharField(max_length=100, blank=True)
    bedrooms = models.CharField(max_length=100, blank=True)
    bathrooms = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    territory = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.URLField(blank=True)
    front_description = models.TextField(blank=True, max_length=100, help_text='Listings page description. Short description of property')
    back_description = models.TextField(blank=True, max_length=1000, help_text='Detailed description. Long description of property')
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        path = reverse('propdetails', args=[self.pk])
        return path
    
class Transaction(models.Model):
    Property = models.ForeignKey(Listing, on_delete=models.CASCADE, primary_key=False)
    Buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    Method = models.CharField(max_length=100)
    price = models.IntegerField()
    Complete = models.BooleanField()
    def get_absolute_url(self):
        return reverse('buy', args=[self.pk])
class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.IntegerField()