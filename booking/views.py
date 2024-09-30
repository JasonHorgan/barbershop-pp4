from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm


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

def appointments(request):
    """
    Renders appointments page
    """
    return render(request, "appointments.html")

def profile(request):
    """
    Renders appointments page
    """
    bookings = Appointment.objects.filter(author=request.user)
    return render(request, "profile.html", 
    {'bookings': bookings})

def book_appointment(request):
    """
    Renders book_appointment page and form
    """
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)  # Create a new instance without saving it yet
            appointment.author = request.user  # Set the author to the current user
            appointment.save()  # Save the appointment to the database
            return redirect('profile')
    else:
        form = AppointmentForm()

    return render(request, "book_appointment.html", {"form": form})


        
