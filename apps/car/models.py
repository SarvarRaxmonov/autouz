from django.contrib.auth.models import User
from django.db import models


class Marka(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class ModelOfCar(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


CURRENCY_CHOICES = (
    ("usd", "USD"),
    ("eur", "EUR"),
    ("uzs", "UZS"),
)


class CarDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    modeli = models.ForeignKey(ModelOfCar, on_delete=models.CASCADE)
    price = models.BigIntegerField(default=0)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default="uzs")
    image = models.ImageField(upload_to="images/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.marka.name
