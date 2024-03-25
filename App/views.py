from django.shortcuts import render
from App.models import allpets

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
