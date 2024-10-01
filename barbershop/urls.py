

"""
URL configuration for barbershop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from booking.views import index 
from booking.views import services 
from booking.views import about
from booking.views import appointments
from booking.views import book_appointment
from booking.views import edit_appointment
from booking.views import profile
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('about/', about, name= 'about'),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('appointments/', appointments, name="appointments"),
    path("", index, name = 'home'),
    path('services/', services, name= 'services'),
    path('book_appointment/', book_appointment, name="book_appointment"),
    path('profile/', profile, name="profile"),
    path('edit_appointment/', edit_appointment, name="edit_appointment")
    
]
