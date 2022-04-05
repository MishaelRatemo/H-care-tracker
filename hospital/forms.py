from ctypes.wintypes import HACCEL
from dataclasses import field, fields
from django import forms
from .models import Hospital
#......
class RequestForm(forms.ModelForm):
    class Meta:
        # model = Hospital
        # exclude = ['user','hospital_name']
        model = Hospital
        fields= []
