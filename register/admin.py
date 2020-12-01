from django.contrib import admin

# Register your models here.
from main.models import Player, Media

#!I have trouble registering the form. I think only forms are generally allowed.
#?I think there is trouble registering classes with meta
admin.site.register(Player)
admin.site.register(Media)