from django.contrib import admin
from apps.car.models import CarDetail, Marka, ModelOfCar


admin.site.register(Marka)
admin.site.register(ModelOfCar)
admin.site.register(CarDetail)
