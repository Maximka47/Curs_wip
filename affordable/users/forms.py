from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User

class UserSigninForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'password']
