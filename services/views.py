from django.shortcuts import render
from .service_layer import get_active_services

def services_list(request):
    services = get_active_services()
    return render(request, "services/services_list.html", {"services": services})

