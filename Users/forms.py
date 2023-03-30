from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Profile
class ProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']