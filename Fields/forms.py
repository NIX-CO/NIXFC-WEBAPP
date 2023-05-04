from django import forms
from .models import Field


class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ('name', 'size', 'image', 'latitude', 'longitude', 'organization')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-select'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'organization': forms.Select(attrs={'class': 'form-select'}),
        }


        
class FieldDeleteForm(forms.Form):
    field_id = forms.IntegerField()        
