from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class SettingsView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
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
    success_url = reverse_lazy('table')
    template_name = 'settings.html'
    #form_class = CustomUserChangeForm

    def test_func(self):
        logged_in_user = self.request.user.pk
        return logged_in_user == self.kwargs.get('pk')
