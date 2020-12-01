from django.shortcuts import render, redirect
from .models import Player, Media
from django.http import HttpResponseRedirect
import time

# Create your views here.
def home(response):
    #!I need to check if there is a post action in home
    if response.method == "POST":
        return redirect("/play")
    else:
        if response.user.is_authenticated:
            #!Id can always be 1 becuase there will never be more than 1
            #?Weird matching query doesn't exist error
            #?I think I will have to import registration form because names are unique and I need to get the correct one.
            u = Player.objects.get(id=response.user.id)

            return render(response, "main/home.html", {"user": u, "logged_in": True})
        
        else:
            #?I think I can try creating a new class in models which is for an anonymous user
            #?An anonymous user will have a specific value turned on

            return render(response, "main/home.html", {"logged_in": False})


#*This going to be the actual play method.
def five_sec_timer():
    global time_remaining_int
    #*time.sleep here doesn't work well cuz it kinda freezes the whole website.
    #!Plus the numbers don't get updated
    time.sleep(100)
    time_remaining_int -= 1

#*It's difficult to just refresh the website again and again becuase play() can only be called when website is refreshed

time_remaining_int = 5

def play(response):
    global time_remaining_int
    #!I am pretty sure this method only gets called when it is refreshed. 
    #*Maybe response is updated
    #Building a timer
    #*Option 1: connect variables using global variables. Five sec timer will call play every second
    if response.user.is_authenticated:
        #!Id can always be 1 becuase there will never be more than 1
        #?Weird matching query doesn't exist error
        #?I think I will have to import registration form because names are unique and I need to get the correct one.
        u = Player.objects.get(id=response.user.id)
        media = Media.objects.get(id=1)
        
        #*I don't know how to just modify the webpage without refreshing it.
        #*Many websites say I need javascript to do this.
        #!I think I will have to learn some basic javascript to do this.
        #*Then I will connect the javascript to html and django
        time_remaining_int -= 1
        
        return render(response, "main/play.html", 
        {"user": u, 
        "logged_in": True,
        "media": media, 
        "current_score": None,
        "previous_highscore": None,
        "time_remaining_label": None,   
        "time_remaining_int": time_remaining_int,
        "audio": None,
        "label_colour": None,
        "label_font": None, 
        "textbox_colour": None, 

        })

    else:
        return redirect('/')

    