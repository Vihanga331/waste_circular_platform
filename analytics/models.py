from django.db import models


class SustainabilityMetrics(models.Model):
    household = models.ForeignKey("households.Household", on_delete=models.CASCADE, null=True, blank=True)
    district = models.CharField(max_length=80)
    recycling_score = models.DecimalField(max_digits=5, decimal_places=2)
    carbon_reduction_kg = models.DecimalField(max_digits=10, decimal_places=2)
    landfill_reduction_kg = models.DecimalField(max_digits=10, decimal_places=2)
    segregation_score = models.DecimalField(max_digits=5, decimal_places=2)
    measured_on = models.DateField()


class Notification(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="notifications")
    title = models.CharField(max_length=160)
    body = models.TextField()
    category = models.CharField(max_length=60)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
