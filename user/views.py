from django.forms import ValidationError
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from rest_framework.authtoken.models import Token
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .repository import CustomUserRepository
from .serializers import CustomUserSerializer
from .forms import UserForm

# Login
class CustomLoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('books-list')  

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        token, created = Token.objects.get_or_create(user=user)
        return redirect(self.get_success_url())

class ListUserView(TemplateView):
    template_name = 'users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['is_authenticated'] = self.is_authenticated
        try:
            books = CustomUserRepository().get_all_users()
            serializer = CustomUserSerializer(books, many=True)
            context['users'] = serializer.data

            name = self.request.GET.get('name')

            if name:
                filters = {}
                filters['name__icontains'] = name
                books = CustomUserRepository().filter_user(filters)
                serializer = CustomUserSerializer(books, many=True)
                context['users'] = serializer.data
        except ValidationError as e:
            context['errors'] = e
        except Exception as e:
            context['errors'] = e
        return context
    
class CreateUserView(TemplateView):
    template_name = 'createUser.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserForm()
        return context

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            serializer = CustomUserSerializer(data=data)
            if  serializer.is_valid():
                CustomUserRepository().create_user(data)
                return redirect('users-list')
            else:
                context = self.get_context_data(**kwargs)
                context['form'] = form
                context['serializer_errors'] = serializer.errors
                return self.render_to_response(context)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['errors'] = form.errors 
        return self.render_to_response(context)