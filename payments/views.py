from django.urls import reverse
from venv import create
from django.shortcuts import render, redirect
from .models import Listings, Transaction
# Create your views here.
def Listings(request):
    model = list(Listings.objects.all())
    mainlist = []
    for i in range(len(model)):
        dict1 = dict(model[i])
        data = {
            'name': dict1['name'],
            'price': dict1['price'],
            'location': dict1['location'],
            'image': dict1['image'],
            }
        mainlist.append(data)
    return render(request, 'listings.html', {'mainlist': mainlist})
def buy(request):
    if request.method == 'POST':
        property = request.POST['property']
        model = Listings.objects.get(id=property)
        createtransaction = CreateTransaction(request, model)
        return redirect(reverse('methodselect'))
def CreateTransaction(request, property):
    model = Transaction()
    model.Property = property
    model.Buyer = request.user  
    model.Complete = False
    model.method = 'N/A'
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
    model2 = Listings.objects.get(id=model.Property.id)
    model2.Owner = model.Buyer
    model2.save()
    model.save()
    return render(request, 'success.html')