from django.shortcuts import render
from . models import Program

def uni_listing(request):
    universities = Program.objects.all()
    return render(request, 'uni-listings.html', {'offerings':universities})

# Create your views here.
