# views.py
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from rest_framework.authtoken.models import Token
from django.shortcuts import redirect
from django.urls import reverse_lazy

class CustomLoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('books-list')  # Redirecionar para a URL após o login bem-sucedido

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        token, created = Token.objects.get_or_create(user=user)
        # Aqui você pode adicionar o token ao contexto ou redirecionar com o token
        return redirect(self.get_success_url())
