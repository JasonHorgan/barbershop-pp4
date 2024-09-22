from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):
    service = models.CharField(max_length=200, unique=True)
    barber = models.SlugField(max_length=200, unique=True)
    date = models.DateField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
)
    created_on = models.DateTimeField(auto_now_add=True)

class Barber(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Services(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


