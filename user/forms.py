from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'email', 'password']
        labels = {
            'name': 'Nome completo',
            'username': 'Usuário',
            'email': 'E-mail',
            'password': 'Senha'
        }

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = [ 'username', 'password']
        labels = {
            'username': 'Usuário',
            'password': 'Senha'
        }