from django.shortcuts import render , redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render (request, 'index.html')

def login(request):
    return render (request, 'login.html')

def logout(request):
    return render (request, 'index.html')