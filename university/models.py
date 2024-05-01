from django.db import models

# Create your models here.
class Uni_Listing(models.Model):
    University = models.CharField(max_length=100)
    Program = models.CharField(max_length=100)
    location_local = models.CharField(max_length=100)
    location_broad = models.CharField(max_length=100)
    tuition = models.CharField(max_length=100)
    Bachelor = models.BooleanField(blank=True)
    Associate = models.BooleanField(blank=True)
    Masters = models.BooleanField(blank=True)
    PhD = models.BooleanField(blank=True)
    Enrollment_Start = models.CharField(max_length=100)
    Enrollment_End = models.CharField(max_length=100)
    Description = models.TextField(max_length=1000)
    Max_Capacity = models.CharField(max_length=100)
    Max_Applications = models.CharField(max_length=100)
