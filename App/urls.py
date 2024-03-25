
from django.urls import path
from App import views

urlpatterns = [
    path("",views.index,name="home"),
    path("aboutUs",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("loginp",views.loginp,name="loginp"),
    path("signupp",views.signupp,name="signupp"),
    path("search",views.searchpet,name="search"),

]