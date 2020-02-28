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

    # def update(self, instance, validated_data):
    #     """
    #     Allow user to partial update
    #     TODO: see all the ways to partially update
    #     """
    #     instance.gender = validated_data.get('gender', instance.gender)
    #     instance.age = validated_data.get('age', instance.age)
    #     instance.like_ingredients = validated_data.get('like_ingredients', instance.like_ingredients)
    #     instance.dislike_ingredients = validated_data.get('dislike_ingredients', instance.dislike_ingredients)
    #     instance.like_recipe = validated_data.get('like_recipe', instance.like_recipe)
    #     instance.ok_recipe = validated_data.get('ok_recipe', instance.ok_recipe)
    #     instance.dislike_recipe = validated_data.get('dislike_recipe', instance.dislike_recipe)
    #     instance.save()
    #     return instance
