from rest_framework import serializers
from .models import FoodOptions


class FoodOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOptions
        fields = ('id', 'food')
