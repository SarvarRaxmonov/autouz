from django.urls import path
from apps.car.views import CarViewSet

urlpatterns = [
    path(
        "car-detail/<int:pk>/",
        CarViewSet.as_view({"get": "retrieve"}),
        name="car-detail",
    ),
    path("car-list/", CarViewSet.as_view({"get": "list"}), name="car-list"),
]



