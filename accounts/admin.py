from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class PlatformUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Platform role", {"fields": ("role", "phone", "email_verified", "mfa_enabled")}),)
    list_display = ("username", "email", "role", "email_verified", "mfa_enabled", "is_staff")
