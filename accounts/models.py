from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        CITIZEN = "citizen", "Citizen"
        COLLECTION_WORKER = "collection_worker", "Collection worker"
        METHANE_OPERATOR = "methane_operator", "Methane plant operator"
        ADMIN = "admin", "Admin"
        GOVERNMENT_OFFICER = "government_officer", "Government officer"

    role = models.CharField(max_length=40, choices=Role.choices, default=Role.CITIZEN)
    phone = models.CharField(max_length=30, blank=True)
    email_verified = models.BooleanField(default=False)
    mfa_enabled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
