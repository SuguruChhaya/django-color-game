from django.shortcuts import render, redirect
from main.models import Player
from django.contrib.auth import login, authenticate
from .forms import  RegistrationForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            #*Creating new RegistrationForm object which we will store in our database
            n = form.cleaned_data['username']
            p = Player(name=n)
            p.save()
            response.user.player.add(p)
            #*Logging in by default
            #!Cannot forget to save the form itself because authentication won't work otherwise
            form.save()
            return redirect("/login")
    else:
        form = RegistrationForm()

    if response.user.is_authenticated:
        u = Player.objects.get(id=response.user.id)
        return render(response, "register/register.html", {"form": form, "user": u, "logged_in": True})

    else:
        return render(response, "register/register.html", {"form": form, "logged_in": False})
    
    #*I can check user here as well
    

