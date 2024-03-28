from django.shortcuts import render,redirect
from App.models import allpets
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from App.models import contactus
from django.contrib import messages


# Create your views here.

# index page
def index(request):
        return render (request,"index.html")

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
        return render(request,"all.html",{"pets":searchdata})
def contactsave(request):
        if request.method == "POST":
                name=request.POST.get("c-name")
                email=request.POST.get("c-email")
                msg=request.POST.get("c-msg")
                messageemail=f"""

                customer Name={name}
                 customer email={email}
                
                 customer message={msg}.

contact them as soon as possible..................:)"""
                mail = EmailMessage("contact him", messageemail, "creative07vibez@gmail.com ", ["rohitpatial121@gmail.com",{email}])
                mail.send()

                mydata = contactus(name = name, email = email, msg=  msg)
                mydata.save()
                return redirect("home")

def all(request):
        pets = allpets.objects.all
        return render(request,"all.html",{'pets': pets})


def signupdata (request):
        if request.method == "POST":
            FullName = request.POST.get("s-name")
            username = request.POST.get("s-username")
            email = request.POST.get("s-email")
            Password = request.POST.get("s-password")
           

            saveuser = User.objects.create_user(username = username, email = email, password=Password, first_name = FullName)
            saveuser.save()

        return render(request, "login.html")

def loginto(request):
       if request.method=="POST":
         name = request.POST.get("l-username")
         passx = request.POST.get("l-password")
    
         usercheck = authenticate(username=name, password=passx)

         if usercheck is not None:
             login(request, usercheck)
             messages.success(request, "Login Sucessfully done..!")
             return redirect('home')
        
         else:
             messages.warning(request, "PLease Enter vaild Crentationals!.... ")

def logouthere(request):
        logout(request)
        return redirect("login")




       
