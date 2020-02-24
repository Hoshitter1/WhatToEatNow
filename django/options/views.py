from rest_framework import generics
from .serializers import FoodOptionSerializer
from .models import FoodOptions


class FoodOptionsView(generics.ListCreateAPIView):
    serializer_class = FoodOptionSerializer
    queryset = FoodOptions.objects.all()
