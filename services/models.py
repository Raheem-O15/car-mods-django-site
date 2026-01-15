from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ("interior", "Interior Modification"),
        ("exterior", "Exterior Modification"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
