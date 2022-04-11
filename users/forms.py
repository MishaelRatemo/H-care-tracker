from django import forms
from django.contrib.auth.models import User
from tracker.models import Profile

class SignupForm(forms.Form):
    """signup form"""

    username = forms.CharField(
        min_length=5,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control'})
    )
    password = forms.CharField(
        min_length=8,
        max_length=70,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'})
    )
    password_confirmation = forms.CharField(
        min_length=8,
        max_length=70,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation','class': 'form-control'})
    )
    first_name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'First name','class': 'form-control'})
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Last name','class': 'form-control'})
    )
    email = forms.CharField(
        min_length=7,
        max_length=70,
        widget=forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-control'})
    )
    facility = forms.CharField(
        min_length=5,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Place of work','class': 'form-control'})
    )
    account_type = forms.CharField(
        widget=forms.Select(attrs={'placeholder': 'Pick one','class': 'form-control'})

    )
    
    def clean_username(self):
        """username must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        '''verify password confirmation match'''
        data = self.cleaned_data
        data.pop('password confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

class LoginForm(forms.Form):
    """login form"""
    
    username = forms.CharField(
        min_length=5,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control'})
    )
    password = forms.CharField(
        min_length=8,
        max_length=70,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'})
    )