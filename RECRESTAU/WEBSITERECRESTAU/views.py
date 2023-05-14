from django.shortcuts import render,redirect
import requests
#from django.contrib.auth import authenticate, login
from .models import Restaurant
# Create your views here.
def home(request):
    return render(request, 'home.html')
#def signup(request):
    #return render(request, 'signup.html')

#def login(request):
        #return render(request, 'login.html')
def service(request):
        restaurants = Restaurant.objects.all()
        return render(request,'service.html',context={"restaurants":restaurants})
