from django import forms
from .models import *
class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = (
            'imputShortName',
            'imputShortNumber',
        )