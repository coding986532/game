from django.shortcuts import render
from . models import Programs

def uni_listing(request):
    universities = Programs.objects.all()
    return render(request, 'uni-listings.html', {'offerings':universities})

# Create your views here.
