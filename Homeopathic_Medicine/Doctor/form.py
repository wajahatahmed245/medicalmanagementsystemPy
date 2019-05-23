from django import forms
from django.contrib.auth.models import User


class MyRegistrationForm(forms.RegistrationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username' : forms.TextInput(attrs = {'class': 'form-control'}),
            'password' : forms.PasswordInput(attrs = {'class': 'form-control'})
        }