from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Player

class PlayerForm(UserCreationForm):
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Player
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'bio', 'photo', 'weight','height', 'position', 'phone']
