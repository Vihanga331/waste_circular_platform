from django.db import models


class RecyclingInventory(models.Model):
    material = models.CharField(max_length=80)
    category = models.CharField(max_length=80)
    weight_kg = models.DecimalField(max_digits=10, decimal_places=2)
    contamination_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    estimated_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    warehouse_location = models.CharField(max_length=120)
    updated_at = models.DateTimeField(auto_now=True)
