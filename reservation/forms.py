from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['field', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.TextInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.TextInput(attrs={'type': 'datetime-local'}),
        }
