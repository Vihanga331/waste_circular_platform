from django.db import models


class Billing(models.Model):
    household = models.ForeignKey("households.Household", on_delete=models.CASCADE)
    period = models.CharField(max_length=20)
    base_fee = models.DecimalField(max_digits=10, decimal_places=2)
    recycling_credit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    methane_credit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)


class Payment(models.Model):
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE, related_name="payments")
    reference = models.CharField(max_length=80, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=40)
    paid_at = models.DateTimeField(auto_now_add=True)
