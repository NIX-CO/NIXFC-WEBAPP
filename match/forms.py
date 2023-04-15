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
class MatchDeleteForm(forms.Form):
    confirm = forms.BooleanField(label='Confirm deletion', required=True)   
class MatchFilterForm(forms.Form):
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()

    def filter_matches(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        return Match.objects.filter(date__gte=start_date, date__lte=end_date)        