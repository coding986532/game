from random import choices
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
degreetype = (
    ('Assoicate', 'Assoicate'),
    ('Bacholers', 'Bacholers'),
    ('Masters', 'Masters'),
    ('Doctoral', 'Doctoral'),
)  
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
    Bachelors_Pay = models.IntegerField()
    Associate_Pay = models.IntegerField()
    Masters_Pay = models.IntegerField()
    Doctoral_Pay = models.IntegerField()
    Experience = models.CharField(max_length=500, blank=True, help_text='Number of years in experience.') 
    Title = models.CharField(max_length=500, blank=True)
    Location_Local = models.CharField(max_length=500, blank=True, help_text='Street')
    Location_Broad = models.CharField(max_length=500, blank=True,help_text=' City, State, Zip, Territory')
  
    def get_absolute_url(self):
        path = reverse('jobdetail', args=[self.pk])
        return path
    def applyurl(self):
        return reverse('apply', args=[self.pk])

class Application(models.Model):
    Job = models.ForeignKey(Job, on_delete=models.CASCADE)
    Status = models.BooleanField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)

class Degree(models.Model):
    Holder = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Type = models.CharField(max_length=200, choices=degreetype)
   # From = models.ForeignKey(university, on_delete=models.CASCADE)