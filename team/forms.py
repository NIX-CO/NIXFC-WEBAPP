from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'date', 'logo', 'number_of_members', 'city', 'country']
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'}),
        }