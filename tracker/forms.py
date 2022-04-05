from django import  forms
from tracker.models import Registrations


class RegistrationForm(forms.ModelForm):
   
    class Meta:
        model = Registrations
        fields = '__all__'
        
        
class LoginForm(forms.ModelForm):
       
    class Meta:
        model = Registrations
        fields = ['email','password']