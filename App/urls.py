
from django.urls import path
from App import views

urlpatterns = [
    path("",views.index,name="home"),
    path("aboutUs",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("loginp",views.loginp,name="login"),
    path("signupp",views.signupp,name="signupp"),
    path("search",views.searchpet,name="search"),
    path("contactsave",views.contactsave),
    path("all",views.all,name="all"),
    path("signupdata",views.signupdata,name="signupdata"),
    path("loginto",views.loginto,name="loginto"),
    path("logouthere",views.logouthere,name="logouthere"),
    

]