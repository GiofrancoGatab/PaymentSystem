from django.db import models
from django.utils import timezone

class Payment(models.Model):
    card_number = models.CharField(max_length=20)
    cardholder_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    action = models.CharField(max_length=10)  # 'deposit' or 'withdraw'
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)  # <--- Add this field