from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
import jwt
from datetime import datetime, timedelta
import uuid
import hashlib
from pathlib import Path
import os
import rsa
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
pubkeypath=os.path.join(BASE_DIR, 'public.pem')
privatekeypath=os.path.join(BASE_DIR, 'priavte.pem')
# Create your views here.
def logout_user(request):
    if request.method != "POST":
        return render(request, "registration/logout.html")
    else:
        logout(request)
        return redirect('/')
def apilogon(request):
    if request.method == 'POST':
        dict = json.loads(request.body)
        user = authenticate(request, username=dict.user, password=dict.pw)
        if user is not None:
            expiration_time = datetime.now(datetime.utc) + timedelta(days=1)
            uuid = str(uuid.uuid4())
            hashuuid = hashlib.sah256(uuid).digest()
            with open(privatekeypath, 'rb') as private:
                priavte_key = rsa.PrivateKey.load_pkcs1(private.read(), format='PEM')
            with open(pubkeypath, 'rb') as public:
                public_key = rsa.PrivateKey.load_pkcs1(public.read(), format='PEM')
            apitoken = rsa.sign(hashuuid, priavte_key, 'SHA-256')
            secret = b'OIDFJIODSFJIODSFJIU(IOJEOJFODJFOSJDFIOSJDOFIJDSOFIJDSOIJSODIJDOFJ8383mc8rm28xmf8emdbitacoindf8asdfmunchymicrosfotgood)'
            jwtdict={
                'user': dict.user, 
                'exp': expiration_time,
                'apitoken': apitoken,
            }
            token = jwt.encode(jwtdict, secret, algorithm='HS256')
            return JsonResponse({'status': 'Good', 'token': token})
        else:
            return JsonResponse({'status': 'error', 'token':'NULL'}, status=401)
def logon(request):
    if request.method != "POST":
        return render(request, "registration/login.html")
    else:
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(request,  username= username,
        password=password)
        if user is not None :
            login(request, user)
            next_url = request.GET.get('next', '/')
            return redirect(next_url)

        else: 
            context = {
                'error': "Invalid Username or Password"
                }
            return render(request, "registration/login.html", context)
def signup1(request):
    if request.method != "POST":
        return render(request, "registration/signup.html")
    else:
        username = request.POST['Username']
        password = request.POST['Password']
        try:
            user = User.objects.create_user(
        username=  username,
        password=        password
    )
        except Exception:
            context = {
                'error': "User Already Exsits"
                }
            return render(request, "registration/signup.html", context)
        user.save()
        user = authenticate(request,  username= username,
        password=password)
        if user is not None :
            login(request, user)
            next_url = request.GET.get('next', '/')
            return redirect(next_url)