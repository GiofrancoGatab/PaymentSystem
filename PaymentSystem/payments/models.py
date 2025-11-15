from django.db import models
from django.utils import timezone

class Payment(models.Model):
    card_number = models.CharField(max_length=20)
    cardholder_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)  # <-- default added
    action = models.CharField(max_length=10, default='deposit')

    def __str__(self):
        return f"{self.cardholder_name} - {self.amount}"