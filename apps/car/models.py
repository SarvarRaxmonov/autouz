from django.db import models


class Marka(models.Model):
    name = models.CharField(max_length=300)


class ModelOfCar(models.Model):
    name = models.CharField(max_length=300)


class CarDetail(models.Model):
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    modeli = models.ForeignKey(ModelOfCar, on_delete=models.CASCADE)
    price = models.BigIntegerField(default=0)
    image = models.ImageField(upload_to="images/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
