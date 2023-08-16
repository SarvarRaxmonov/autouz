from django.db.models import Avg
from rest_framework import serializers
from .models import CarDetail


class CarDetailSerializer(serializers.ModelSerializer):
    modeli = serializers.CharField(source="modeli.name")
    marka = serializers.CharField(source="marka.name")
    average_price = serializers.SerializerMethodField()
    ratio_in_price = serializers.SerializerMethodField()
    price_position = serializers.SerializerMethodField()

    class Meta:
        model = CarDetail
        fields = (
            "id",
            "marka",
            "modeli",
            "average_price",
            "price",
            "ratio_in_price",
            "price_position",
            "currency",
            "image",
            "created_at",
            "updated_at",
        )

    def get_average_price(self, obj):
        average_price = CarDetail.objects.filter(
            marka=obj.marka, modeli=obj.modeli, currency=obj.currency
        ).aggregate(avg_price=Avg("price"))["avg_price"]

        return average_price

    def get_ratio_in_price(self, obj):
        avg_price = self.get_average_price(obj)
        price_in_difference = obj.price - avg_price
        percentage = int((price_in_difference / avg_price) * 100)
        if percentage > 0:
            comparison_type = "Expensive"
        elif percentage < 0:
            comparison_type = "Cheaper"
        else:
            comparison_type = "Equal"
        return f"{comparison_type} : {abs(price_in_difference)} {obj.currency} ({percentage} %)"

    def get_price_position(self, obj):
        percentage = int((obj.price * 100) / self.get_average_price(obj))
        return f"{percentage} %"
