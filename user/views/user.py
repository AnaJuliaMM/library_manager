from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..serializers.user import UserLoginSerializer
from ..repository.user_repository import UserRepository
from django import forms

# Definindo um formulário de login
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class UserLoginPage(viewsets.ViewSet):
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        form = UserLoginForm()
        return render(request, 'login.html', {"form": form})

class UserLoginView(viewsets.ViewSet):
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = UserRepository.get_user_by_username(username)
            if user and UserRepository.validate_password(user, password):
                login(request, user)
                return redirect('home')  # Redireciona para a página inicial ou outra página após o login bem-sucedido
            
            errors = {"form_errors": "Invalid credentials"}
            return render(request, 'login.html', {'form': form, 'errors': errors})
        
        return render(request, 'login.html', {'form': form, 'errors': form.errors})
