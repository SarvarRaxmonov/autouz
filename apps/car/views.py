from rest_framework import viewsets
from .models import CarDetail
from .serializers import CarDetailSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = CarDetail.objects.all()
    serializer_class = CarDetailSerializer
