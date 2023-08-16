from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import CarDetail
from .serializers import CarDetailSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = CarDetail.objects.all()
    serializer_class = CarDetailSerializer
