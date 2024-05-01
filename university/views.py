from django.shortcuts import render
from . models import Program

def uni_listing(request):
    offerings = Program.objects.all()
    return render(request, 'uni-listings.html', {'offerings':offerings})

# Create your views here.
