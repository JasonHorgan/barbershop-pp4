from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required


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

@login_required
def profile(request):
    """
    Renders appointments page
    """
    bookings = Appointment.objects.filter(author=request.user)
    return render(request, "profile.html", {'bookings': bookings})


@login_required
def edit_appointment(request, appointment_id):
    """
    Allows users to edit an existing appointment.
    """
    appointment = get_object_or_404(Appointment, id=appointment_id,
                                    author=request.user)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
        messages.success(request, ('Your booking has been' +
                                   'updated successfully'))
        return redirect('profile')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, "edit_appointment.html",
                  {"form": form, "appointment": appointment})


@login_required
def book_appointment(request):
    """
    Renders book_appointment page and form
    """
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.author = request.user
            appointment.save()
            return redirect('profile')
    else:
        form = AppointmentForm()

    return render(request, "book_appointment.html", {"form": form})


@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id,
                                    author=request.user)

    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Your booking has been cancelled')
        return redirect('profile')

    # Render a confirmation page if the request is not a POST request
    return render(request, "confirm_cancellation.html",
                  {"appointment": appointment})
