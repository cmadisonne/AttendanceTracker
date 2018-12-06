from .models import clockOut, clockIn
from django import forms

class clockInForm(forms.ModelForm):
    class Meta:
        model = clockIn
        fields = {'username', 'password', 'clockIn'}
        widgets = {
            'password': forms.PasswordInput(),
            'clockIn': forms.HiddenInput(),
        }

class clockOutForm(forms.ModelForm):
    class Meta:
        model = clockOut
        fields = {'username', 'password', 'clockOut'}
        widgets = {
            'password': forms.PasswordInput(),
            'clockOut': forms.HiddenInput(),
        }

