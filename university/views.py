from django.shortcuts import render
from . models import Program
from django.urls import reverse

 
def uni_listing(request): 
    offerings = Program.objects.all()
    return render(request, 'uni-listings.html', {'offerings':offerings})

def uni_listing_detail(request, pk):
    offerings = Program.objects.get(pk=pk)
    return render(request, 'uni-listing-detail.html', {'offerings':offerings})
# Create your views here.
