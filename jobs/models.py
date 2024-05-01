from django.db import models
from django.urls import reverse

# Create your models here.
class Job(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
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
    Experience = models.CharField(max_length=500, blank=True, help_text='Number of years in experience.') 
    Title = models.CharField(max_length=500, blank=True)
    Location_Local = models.CharField(max_length=500, blank=True, help_text='Street, City, Zip')
    Location_Broad = models.CharField(max_length=500, blank=True,help_text='State, Territory, Country')

    def get_absolute_url(self):
        path = reverse('jobdetail', args=[self.pk])
        return path


