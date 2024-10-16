from .models import Appointment
from django import forms
from django.forms import ModelForm 

class AppointmentForm(forms.ModelForm):
    TIME_CHOICES = [
        ('09:00', '09:00 AM'),
        ('11:00', '11:00 AM'),
        ('14:00', '02:00 PM'),
        ('16:00', '04:00 PM'),
    ]

    time = forms.ChoiceField(choices=TIME_CHOICES, label="Choose a Time Slot")

    class Meta:
        model = Appointment
        fields = ('service', 'barber', 'date', 'time')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

        