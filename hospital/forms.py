from ctypes.wintypes import HACCEL
from django import forms
from .models import Hospital
#......
class RequestForm(forms.ModelForm):
    class Meta:
        model = Hospital
        exclude = ['user','hospital_name']
