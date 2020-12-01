"""game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as v
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('register/', v.register),
    #!This automatically looks for a login.html and does the process for us
    #!Create a registration folder in one of the templates folder (I created it in )
    #!I have to name the login folders 'registration'
    #*I wanna show users in this case too. 
    #!I need to get the response variable for the user id for this case too
    path('', include("django.contrib.auth.urls"))
    
    #*In order to store my media on my server , I have to add it here
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #*First parameter: where you want to find media, where are those files stored
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
