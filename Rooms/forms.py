from django import forms
from django.contrib.auth.models import User
from .models import Room,Field

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['field']

class AddUserForm(forms.Form):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
class RoomFilterForm(forms.Form):
    field = forms.ModelChoiceField(queryset=Field.objects.all(), required=False)    
class AddUserToRoomForm(forms.Form):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple, initial=[])

    def __init__(self, *args, **kwargs):
        room = kwargs.pop('room')
        super(AddUserToRoomForm, self).__init__(*args, **kwargs)
        self.fields['users'].queryset = User.objects.exclude(id__in=room.users_list.all())

        # Set initial values for existing users in the room
        for user in room.users_list.all():
            self.fields['users'].initial.append(user.id)
