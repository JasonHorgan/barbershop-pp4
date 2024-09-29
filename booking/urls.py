from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('/services', views.services, name='services'),
    path('/about', views.about, name='about'),
    path('/appointments', views.appointments, name="appointments"),
    path("accounts/", include("allauth.urls")),
    path('/myappointments', views.myappointments, name="myappointments")

]

