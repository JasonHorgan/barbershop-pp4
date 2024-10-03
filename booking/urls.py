from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('/services', views.services, name='services'),
    path('/about', views.about, name='about'),
    path('/appointments', views.appointments, name="appointments"),
    path("accounts/", include("allauth.urls")),
    path('/book_appointment', views.book_appointment, name="book_appointment"),
    path('/profile', views.profile, name="profile"),
    path('edit_appointment/<int:appointment_id>/', views.edit_appointment, name='edit_appointment'),


]

