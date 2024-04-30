from django.db import models

# Create your models here.
class Joblisting(models.Model):
    Listing_Name = models.CharField(max_length=250)
    Employer = models.CharField(max_length=250)
    Government_Agency = models.BooleanField(blank=True)
    Salary = models.CharField(max_length=50, blank=True)
    Bachelors = models.CharField(max_length=500, blank=True)
    Associate = models.CharField(max_length=500, blank=True)
    Masters = models.CharField(max_length=500, blank=True)
    Doctoral = models.CharField(max_length=500, blank=True)
    Bachelors_Pay = models.CharField(max_length=500, blank=True)
    Associate_Pay = models.CharField(max_length=500, blank=True)
    Masters_Pay = models.CharField(max_length=500, blank=True)
    Doctoral_Pay = models.CharField(max_length=500, blank=True)

