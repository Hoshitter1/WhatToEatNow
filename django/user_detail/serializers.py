from typing import List

from rest_framework import serializers
from .models import UserDetail


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        lookup_field = 'slug'
        fields = (
            'slug',
            'gender',
            'age',
            'like_ingredients',
            'ok_ingredients',
            'dislike_ingredients',
            'like_recipe',
            'ok_recipe',
            'dislike_recipe'
        )
        # read_only_user

        # def update(self, instance, validated_data):
        #     """
        #     Allow user to partial update
        #     TODO: see all the ways to partially update
        #     """
        #     # instance.like_ingredients = validated_data.get('like_ingredients', instance.like_ingredients)
        #     # self.str_list_validation(instance)
        #     # instance.dislike_ingredients = validated_data.get('dislike_ingredients', instance.dislike_ingredients)
        #     # instance.like_recipe = validated_data.get('like_recipe', instance.like_recipe)
        #     # instance.ok_recipe = validated_data.get('ok_recipe', instance.ok_recipe)
        #     # instance.dislike_recipe = validated_data.get('dislike_recipe', instance.dislike_recipe)
        #     return instance

    # def str_list_validation(self, instance):
    #     target_raw = instance.like_ingredients
    #     target_processed = target_raw[1:-1].split(',')
    #     if not isinstance(target_processed, list):
    #         raise Exception('Type is invalid')

    def validate(self, data: dict):
        """
        Expected data
        'apple,egg,etc...' str comma str comma ...
        Unexpected data
        e.g 1 'apple(,egg,..'
        e.g 2 '(apple),egg,...'
        each character has to be in pure name without any other strings
        """
        # TODO:Add validator for recipe
        # target_key_recipe = [
        #     'like_recipe',
        #     'ok_recipe',
        #     'dislike_recipe'
        # ]
        target_key_ingredients = [
            'like_ingredients',
            'dislike_ingredients',
            'ok_ingredients'
        ]
        ingredients_fractal: List[List[str]] = [
            data.get(key).split(',')  # TODO: This needs validation too
            for key in target_key_ingredients
            if data.get(key, None) is not None  # for partial update
        ]
        ingredients_flat: List[str] = [
            data_inner
            for data_list in ingredients_fractal
            for data_inner in data_list
        ]
        for ingredients_word in ingredients_flat:
            if len(ingredients_word) > 20: # TODO: Update the number
                raise serializers.ValidationError("length of ingredients_word is too long")
            has_invalid_char = ',' in ingredients_word  # TODO: Use regular expression and include numbers and other symbols
            if has_invalid_char:
                raise serializers.ValidationError("type of ingredients_word is invalid ")
        return data
