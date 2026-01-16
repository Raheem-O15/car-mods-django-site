from django.urls import path
from .views import home, contact, bookings

urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("bookings/", bookings, name="bookings"),
]
