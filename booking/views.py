from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

#def my_barbershop(request):
 #   return HttpResponse("Hello, Barbershop!")

def index(request):
    """
    Renders Home Page.
    """
    return render(request, "index.html",)

def services(request):
    """
    Renders Services Page.
    """
    return render(request, "services.html",)

def about(request):
    """
    Renders about page
    """
    return render(request, "about.html",)