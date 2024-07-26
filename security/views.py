from operator import truediv
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
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.serialization import load_pem_public_key
import base64
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
pubkeypath=os.path.join(BASE_DIR, 'public.pem')
privatekeypath=os.path.join(BASE_DIR, 'private.pem')
# Create your views here.
def logout_user(request):
    if request.method != "POST":
        return render(request, "registration/logout.html")
    else:
        logout(request)
        return redirect('/')
def apitokencheck(jwtdict):

    token1 = bytes(jwtdict['apitoken'],'UTF-8')
    with open(pubkeypath, "rb") as key_file:
        public_key = load_pem_public_key(key_file.read())
    signature = bytes.fromhex(jwtdict['apitokensig'])
    try:
        public_key.verify(
        signature,
        token1,
        ec.ECDSA(hashes.SHA256())
    )
        return True
    except Exception:
        return False






def apilogon(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)  # For debugging purposes

            # Extract username and password from the dictionary
        username = data.get('user')
        password = data.get('pw')

            # Authenticate the user
        user = authenticate(request, username=username, password=password)
    if user is not None:
            expiration_time = datetime.utcnow() + timedelta(days=1)
            uuid2 = bytes(str(uuid.uuid4()), 'UTF-8')

            with open(privatekeypath, 'rb') as private:
                private_key = load_pem_private_key(private.read(), password=None)

            apitoken =  private_key.sign(
            uuid2,
            ec.ECDSA(hashes.SHA256())
)
            jwtdict = {
                    'user': username,
                    'exp': expiration_time.isoformat(),
                    'apitoken': uuid2.decode('utf-8'),
                    'apitokensig': apitoken.hex(),  # Convert to hex for easier reading
                    'Privlages': [
                        "Buy Property",
                        "Read All",
                    ]
                }

            return JsonResponse({'status': 'Good', 'token': jwtdict})
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