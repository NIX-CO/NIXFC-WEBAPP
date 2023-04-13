from django import forms
from .models import Match

class MatchForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('complete', 'Complete'),
        ('encours', 'En cours'),
        ('annule', 'Annulé'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Match
        fields = ['teamhome', 'teamaway', 'scorehome', 'scoreaway', 'date', 'status']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }