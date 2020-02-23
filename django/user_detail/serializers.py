from rest_framework import serializers
from .models import UserDetail


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = (
            'user',
            'gender',
            'age',
            'like_ingredients',
            'ok_ingredients',
            'dislike_ingredients',
            'like_recipe',
            'ok_recipe',
            'dislike_recipe'
        )
