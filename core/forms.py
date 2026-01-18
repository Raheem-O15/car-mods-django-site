from django import forms
from django.utils import timezone
from .models import Booking


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "w-full border rounded p-2"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "w-full border rounded p-2"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "w-full border rounded p-2"})
    )


class BookingForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "w-full border rounded p-2"}
        )
    )

    class Meta:
        model = Booking
        fields = ["name", "email", "service", "date"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full px-3 py-2 rounded border border-zinc-300 text-black placeholder-zinc-400 focus:outline-none focus:border-black focus:ring-1 focus:ring-black transition"
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full px-3 py-2 rounded border border-zinc-300 text-black placeholder-zinc-400 focus:outline-none focus:border-black focus:ring-1 focus:ring-black transition"
            }),
            "service": forms.Select(attrs={
                "class": "w-full px-3 py-2 rounded border border-zinc-300 bg-white text-black focus:outline-none focus:border-black focus:ring-1 focus:ring-black transition"
            }),
            "date": forms.DateInput(attrs={
                "type": "date",
                "class": "w-full px-3 py-2 rounded border border-zinc-300 bg-white text-black focus:outline-none focus:border-black focus:ring-1 focus:ring-black transition"
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        service = cleaned_data.get("service")
        date = cleaned_data.get("date")

        if service and date:
            if Booking.objects.filter(service=service, date=date).exists():
                raise forms.ValidationError(
                    "This service is already booked for that date. Please choose another day."
                )

        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters.")
        return name

    def clean_date(self):
        date = self.cleaned_data["date"]
        if date < timezone.now().date():
            raise forms.ValidationError("You cannot book a date in the past.")
        return date