from django.db import models


class MethaneProduction(models.Model):
    plant_code = models.CharField(max_length=40)
    organic_input_kg = models.DecimalField(max_digits=10, decimal_places=2)
    methane_m3 = models.DecimalField(max_digits=10, decimal_places=2)
    gas_purity_percent = models.DecimalField(max_digits=5, decimal_places=2)
    pressure_bar = models.DecimalField(max_digits=6, decimal_places=2)
    digester_health_percent = models.DecimalField(max_digits=5, decimal_places=2)
    measured_at = models.DateTimeField()


class GasCylinder(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = "available", "Available"
        RESERVED = "reserved", "Reserved"
        DISTRIBUTED = "distributed", "Distributed"
        MAINTENANCE = "maintenance", "Maintenance"

    serial_number = models.CharField(max_length=80, unique=True)
    capacity_kg = models.DecimalField(max_digits=6, decimal_places=2)
    fill_percent = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=32, choices=Status.choices, default=Status.AVAILABLE)
    last_filled_at = models.DateTimeField(null=True, blank=True)
