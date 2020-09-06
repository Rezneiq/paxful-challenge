from django.db import models
from django.contrib.auth.models import User
from utils.conversor import RatesConversor


class Wallet(models.Model):
    address = models.CharField(max_length=35, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address

    def amount_usd(self):
        return RatesConversor().convert_to_usd(self.amount)