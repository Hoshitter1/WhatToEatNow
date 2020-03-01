from django.contrib import admin
from .models import UserDetail


class UserDetailAdmin(admin.ModelAdmin):
    model = UserDetail
    fieldsets = (
        ('User Profile', {'fields': ('slug', 'gender', 'age')}),
        ('Preferences Of Ingredients', {'fields': ('like_ingredients', 'ok_ingredients', 'dislike_ingredients')}),
        ('Preferences Of Recipe', {'fields': ('like_recipe', 'ok_recipe', 'dislike_recipe')}),
    )
    list_display = ['slug', 'gender', 'age']


admin.site.register(UserDetail, UserDetailAdmin)
