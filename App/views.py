from django.shortcuts import render
from App.models import allpets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# index page
def index(request):
        pets = allpets.objects.all
        return render (request,"index.html",{'pets': pets})

def about(request):
        return render(request,"aboutus.html")
def contact(request):
        return render(request,"contactus.html")
def loginp(request):
        return render(request,"login.html")
def signupp(request):
        return render(request,"signup.html")
def searchpet(request):
        srch=request.GET["query"]
        searchdata=allpets.objects.filter(breed=srch)
        return render(request,"index.html",{"pets":searchdata})
       
