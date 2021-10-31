from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
