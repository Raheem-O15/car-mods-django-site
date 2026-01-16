from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "service", "date", "status", "created_at")
    list_filter = ("status", "service", "date")
    search_fields = ("name", "email")
    list_editable = ("status",)  