from django.shortcuts import render
from .models import Job

# Create your views here.

def joblistings(request):
    jobs = Job.objects.all()
    return render(request, 'joblist.html', {'jobs': jobs})
