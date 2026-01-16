from django.shortcuts import render
from django.conf import settings
from django.utils import timezone
from services.service_layer import get_active_services
from .forms import ContactForm, BookingForm
from django.core.mail import send_mail


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
            booking = form.save()

            send_mail(
                subject="Car Mods Booking Confirmation",
                message=(
                    f"Hi {booking.name},\n\n"
                    f"Your booking for {booking.service.name} on {booking.date} has been received.\n"
                    f"Status: {booking.status.capitalize()}.\n\n"
                    "We’ll contact you shortly.\n\n"
                    "– Car Mods Team"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[booking.email],
                fail_silently=False,
            )

            form = BookingForm()
            form.fields["date"].widget.attrs["min"] = timezone.now().date()

            return render(request, "core/bookings.html", {
                "form": form,
                "success": True
            })
    else:
        form = BookingForm()
        form.fields["date"].widget.attrs["min"] = timezone.now().date()

    return render(request, "core/bookings.html", {"form": form})
