from django.conf import settings
from django.db import models


class WasteCategory(models.Model):
    name = models.CharField(max_length=80)
    code = models.SlugField(unique=True)
    recyclable = models.BooleanField(default=False)
    organic = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class WasteCollection(models.Model):
    class Status(models.TextChoices):
        SCHEDULED = "scheduled", "Scheduled"
        IN_PROGRESS = "in_progress", "In progress"
        VERIFIED = "verified", "Verified"
        REJECTED = "rejected", "Rejected"

    household = models.ForeignKey("households.Household", on_delete=models.CASCADE)
    category = models.ForeignKey(WasteCategory, on_delete=models.PROTECT)
    worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    route_code = models.CharField(max_length=40)
    truck_id = models.CharField(max_length=40)
    weight_kg = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    qr_verified = models.BooleanField(default=False)
    status = models.CharField(max_length=32, choices=Status.choices, default=Status.SCHEDULED)
    collected_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
