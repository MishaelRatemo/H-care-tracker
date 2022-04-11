from django import  forms
from tracker.models import Registrations


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    
    
    class Meta:
        model = Registrations
        fields = '__all__'
        
        
class LoginForm(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    class Meta:
        model = Registrations
        fields = ['email','password']