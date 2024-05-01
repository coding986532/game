from django.shortcuts import render
from . models import Uni_Listing

def uni_listing(request):
    universities = Uni_Listing.objects.all()
    return render(request, 'uni-listings.html', {'offerings':universities})

# Create your views here.
