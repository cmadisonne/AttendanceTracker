from .models import attendanceModel
from django import forms

class attendanceForm(forms.ModelForm):
    class Meta:
        model = attendanceModel
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
            'clockIn': forms.HiddenInput(),
            'clockOut': forms.HiddenInput(),
        }