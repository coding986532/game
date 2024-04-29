from django.urls import reverse
from venv import create
from django.shortcuts import render, redirect
from .models import Listing, Transaction, Balance
# Create your views here.
def home(request):
    listings = Listing.objects.all()
    return render(request, 'home.html', {'listings': listings})
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
    if request.method == 'POST':
        model = Transaction.objects.get(id=request.cookies['transaction'])
        model.method = request.POST['paymethod']
        model.save()
        return redirect(reverse('payment'))
    return render(request, 'methodselect.html')

def payment(request):
    model = Transaction.objects.get(id=request.cookies['transaction'])
    if model.method == 'N/A':
        return Exception
    elif model.Complete != False:
        return Exception
    
    if model.method == 'In Game':
        return render(request, 'ingame.html')
    
def ingamepay(request):
    if request.method != 'post':
        return Exception
    else:
        model2 = Balance.objects.get(User=request.user)
        model = Transaction.objects.get(id=request.cookies['transaction'])
        model2.balance = model2.balance - model.price
        model2.save()
        return redirect(reverse('callback'))
def callback(request):

    model = Transaction.objects.get(id=request.cookies['transaction'])
    model.Complete = True
    model2 = Listing.objects.get(id=model.Property.id)
    model2.Owner = model.Buyer
    model2.save()
    model.save()
    return render(request, 'success.html')