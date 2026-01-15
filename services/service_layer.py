from .models import Service
from .dtos import ServiceDTO

def get_active_services():
    services = Service.objects.filter(is_active=True)
    return [
        ServiceDTO(
            id=s.id,
            name=s.name,
            description=s.description,
            category=s.category,
            is_active=s.is_active
        )
        for s in services
    ]
