from django import forms
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
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date", "class": "w-full border rounded p-2"}))

    class Meta:
        model = Booking
        fields = ["name", "email", "service", "date"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "w-full border rounded p-2"}),
            "email": forms.EmailInput(attrs={"class": "w-full border rounded p-2"}),
            "service": forms.TextInput(attrs={"class": "w-full border rounded p-2"}),
        }