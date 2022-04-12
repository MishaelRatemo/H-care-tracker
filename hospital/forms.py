from ctypes.wintypes import HACCEL
from dataclasses import field, fields
from django import forms

from tracker.models import Order
from .models import Hospital
#......
class RequestForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['user','order_date','item', 'donor_name', 'status']
      
