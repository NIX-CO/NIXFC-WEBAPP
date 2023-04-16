from django import forms
from .models import Field

class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ('name', 'size', 'image','longitude','latitude')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'size': forms.Select(attrs={'class': 'form-control','id': 'size'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file','id': 'formFile'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'id': 'latitude'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'id': 'longitude'}),
        }
        
class FieldDeleteForm(forms.Form):
    field_id = forms.IntegerField()        
