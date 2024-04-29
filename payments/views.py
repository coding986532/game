from django.urls import reverse
from venv import create
from django.shortcuts import render, redirect
from .models import Listing, Transaction
# Create your views here.
def home(request):
    listings = Listing.objects.all()
    return render(request, 'home.html', {'listings': listings})
def details(request, pk):
    listings = Listing.objects.get(pk=pk)
    return render(request, "details.htm", {'data': listings})

def listonsale(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', {'listings': listings})
def buy(request):
    if request.method == 'POST':
        property = request.POST['propertyid']
        model = Listing.objects.get(id=property)
        response = redirect(reverse('methodselect'))
        createtransaction = CreateTransaction(response, model, request.user)
        return response
def CreateTransaction(request, property, user):
    model = Transaction()
    model.Property = property
    model.Buyer = user
    model.Complete = False
    model.method = 'N/A'
    model.price = property.price
    model.save()
    request.cookies['transaction'] = model.id
    return model.id
def methodselect(request):
    return render(request, 'methodselect.html')
def PayMethod(request, transaction, method):
    if request.method == 'POST':
        model = Transaction.objects.get(id=transaction)
        model.method = method
        model.save()
    else:
        return Exception('Error')
def payment(request):
    model = Transaction.objects.get(id=request.cookies['transaction'])
    if model.method == 'N/A':
        return Exception
    elif model.Complete != False:
        return Exception
    
    if model.method == 'In Game':
        return render(request, 'ingame.html')
    

def callback(request):
    model = Transaction.objects.get(id=request.cookies['transaction'])
    model.Complete = True
    model2 = Listing.objects.get(id=model.Property.id)
    model2.Owner = model.Buyer
    model2.save()
    model.save()
    return render(request, 'success.html')