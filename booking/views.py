from django.shortcuts import render
from django.http import HttpResponse
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

def myappointments(request):
    """
    Renders my appointments page
    """
    return render(request, "myappointments.html")

def create_appointment(request):
    if request.method == 'POST':
        # If the form has been submitted, process the data
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Save the appointment to the database
            form.save()
            # Redirect to a success page or somewhere else
            return redirect('myappointments.html')  # You can change 'success_page' to the actual path
    else:
        # If the request is GET, display a blank form
        form = AppointmentForm()

    # Render the form in your template
    return render(request, 'appointments.html', {'form': form})
