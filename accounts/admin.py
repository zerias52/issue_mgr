from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = [
        "username", "email", "role", "team", "is_staff"
    ]
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("email", "role", "team")}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("role", "team")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)