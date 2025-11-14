from django.db import models

class Payment(models.Model):
    cardholder_name = models.CharField(max_length=200)
    card_number = models.CharField(max_length=16)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reference_number} - {self.cardholder_name}"
