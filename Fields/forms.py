from django import forms
from .models import Field

class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ('name', 'size', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }
        
class FieldDeleteForm(forms.Form):
    field_id = forms.IntegerField()        
