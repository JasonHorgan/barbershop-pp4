from django.contrib import admin
from .models import Appointment, Barber

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Barber)
