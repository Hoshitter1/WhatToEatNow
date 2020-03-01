from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Slug shared with detail model', {'fields': ('slug',)}),
        ('Line Account', {'fields': ('nonce_for_line', 'line_message_uid',)}),
    )
    list_display = ['username', 'slug', 'email', 'nonce_for_line', 'line_message_uid']


admin.site.register(CustomUser, CustomUserAdmin)
