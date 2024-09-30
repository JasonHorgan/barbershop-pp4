from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Barber(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, default='SOME STRING')
    

    def __str__(self):
        return self.name

class Services(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100, default='SOME STRING')

    def __str__(self):
        return self.name


class Appointment(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="appointment"
)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user} for {self.services} on {self.date} at {self.time}"