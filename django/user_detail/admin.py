from django.contrib import admin
from .models import UserDetail


class UserDetailAdmin(admin.ModelAdmin):
    model = UserDetail
    fieldsets = (
        ('User Profile', {'fields': ('line_message_uid', 'slug', 'gender', 'age')}),
        ('Preferences Of Ingredients', {'fields': ('like_ingredients', 'ok_ingredients', 'dislike_ingredients')}),
        ('Preferences Of Recipe', {'fields': ('like_recipe', 'ok_recipe', 'dislike_recipe')}),
        ('User History', {'fields': ('recommended_recipe',)}),
    )
    list_display = ['line_message_uid', 'gender', 'age', 'recommended_recipe']


admin.site.register(UserDetail, UserDetailAdmin)
