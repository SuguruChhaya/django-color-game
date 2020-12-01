from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.ForeignKey(User, related_name='player', on_delete=models.CASCADE, null=True)
    #?I wonder if I have to use models.charfield even if I am not actaully displaying the form
    name = models.CharField(max_length=300, null=True)
    #*We want the records to be stored as none if there are no records so I can then change to 0
    previous_record = models.IntegerField(null=True)
    highscore = models.IntegerField(null=True)

#*Since I had trouble importing audio directly, I am going to store audio in a different class
#?I might alos have to store other player related stuff in the models cuz I don't know where else to store them
class Media(models.Model):
    black = models.FileField(blank=True, null=True)
    blue = models.FileField(blank=True, null=True)
    grey = models.FileField(blank=True, null=True)
    green = models.FileField(blank=True, null=True)
    light_blue = models.FileField(blank=True, null=True)
    light_green = models.FileField(blank=True, null=True)
    magenta = models.FileField(blank=True, null=True)
    orange = models.FileField(blank=True, null=True)
    pink = models.FileField(blank=True, null=True)
    purple = models.FileField(blank=True, null=True)
    red = models.FileField(blank=True, null=True)
    white = models.FileField(blank=True, null=True)
    yellow = models.FileField(blank=True, null=True)
