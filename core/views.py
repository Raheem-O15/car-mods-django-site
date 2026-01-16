from django.shortcuts import render
from services.service_layer import get_active_services
from .forms import ContactForm, BookingForm


def home(request):
    return render(request, "core/home.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Contact cleaned data:", form.cleaned_data)
            return render(request, "core/contact.html", {
                "form": ContactForm(),
                "success": True
            })
    else:
        form = ContactForm()

    return render(request, "core/contact.html", {"form": form})


def bookings(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save to database
            form = BookingForm()  # Reset form
            return render(request, "core/bookings.html", {
                "form": form,
                "success": True
            })
    else:
        form = BookingForm()

    return render(request, "core/bookings.html", {"form": form})