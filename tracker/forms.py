from django import  forms
from tracker.models import Registrations


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'autocomplete':'off'}))
    confirm_password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    
    
    class Meta:
        model = Registrations
        fields = '__all__'
        
        
class LoginForm(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    class Meta:
        model = Registrations
        fields = ['email','password']
        
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    