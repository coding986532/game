from django.urls import reverse
from venv import create
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Listing, Transaction, Balance
from jobs.models import Job
from university.models import Program  
# Create your views here.
def home(request):
    jobs = Job.objects.order_by('-created_at')[:3]
    listings = Listing.objects.order_by('-created_at')[:3]
    offerings = Program.objects.order_by('-created_at')[:3]

    return render(request, 'home.html', {'listings': listings, 'jobs': jobs, 'offerings': offerings})

def jobdetail(request, pk):
    jobs = Job.objects.get(pk=pk)
    return render(request, 'jobdetail.html', {'job': jobs})

def details(request, pk):
    listings = Listing.objects.get(pk=pk)
    return render(request, "details.htm", {'listing': listings})

def listonsale(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', {'listings': listings})
def buy(request):
    if request.method == 'POST':
        property = request.POST['propertyid']
        model = Listing.objects.get(id=property)
        
        createtransaction = CreateTransaction(model, request.user)
        response = redirect(reverse('payment', kwargs={'txid': createtransaction}))
        return response
    
def CreateTransaction( property, user):
    model = Transaction()
    model.Property = property
    model.Buyer = user
    model.Complete = False
    model.method = 'N/A'
    model.price = property.price
    model.Method = "In Game"
    model.save()

    return model.id


def payment(request, txid):
    
    model = Transaction.objects.get(id=txid)
    print(model.Method)
    if model.Method == 'N/A':
        return Exception
    elif model.Complete != False:
        return Exception
    
    if model.Method == 'In Game':
        return redirect(reverse('ingamepayemnt', kwargs={'txid': txid}))
    
def ingamepay(request, txid):
    if request.method == 'get':
        return render(request, 'ingame.html')
    elif request.method == 'POST':
        print('post recived ')
        model2 = Balance.objects.get(user=request.user)
        model = Transaction.objects.get(id=txid)
        model2.money = model2.money - model.price
        model2.save()
        return redirect(reverse('callback', kwargs={'txid': txid}))
def callback(request, txid):
    model = Transaction.objects.get(id=txid)
    model.Complete = True
    model2 = Listing.objects.get(id=model.Property.id)
    model2.Owner = model.Buyer
    model2.save()
    model.save()
    return render(request, 'success.html')