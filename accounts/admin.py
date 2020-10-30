from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'university', 'number', 'linkedin_url', 'last_login']
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'university', 'number', 'linkedin_url', 'cv')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'university', 'number', 'linkedin_url', 'cv')}),
    )

    ordering = ('email', 'password', 'first_name', 'last_name', 'university', 'number', 'linkedin_url', 'cv')

admin.site.register(CustomUser, CustomUserAdmin)
