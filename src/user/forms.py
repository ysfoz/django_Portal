from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from django.forms.widgets import PasswordInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label='User Name')
    password = forms.CharField(max_length=20,label='password',widget=PasswordInput)
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
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,label='User Name')
    password = forms.CharField(max_length=20,label ='Password', widget= forms.PasswordInput)
    
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
