from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import PasswordInput

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label='User Name')
    password = forms.CharField(max_length=20,label='password',widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label='Confirm Your Password',widget=PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        
        if password and confirm and password != confirm:
            raise forms.ValidationError('Passwords are not match')
        
        values = {
            'username':username,
            'password':password
        }
        
        return values
    
    
