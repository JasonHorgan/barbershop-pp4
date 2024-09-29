from .models import Appointment
from django import forms
from django.forms import ModelForm 

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('service', 'barber', 'date', 'time')