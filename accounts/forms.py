from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'university',
            'number',
            'linkedin_url',
            'cv',
        )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'university',
            'number',
            'linkedin_url',
            'cv',
        )