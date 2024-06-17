from django.forms import ValidationError
from django.contrib.auth import login,authenticate
from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views import View

from .repository import CustomUserRepository
from .serializers import *
from .forms import UserForm

# Login
class CustomLoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        serializer = LoginSerializer(data=request.POST)
        if serializer.is_valid():
            print(serializer.data)
            user = serializer.validated_data['user']
            print(user)
            login(request, user)
            return redirect('books-list')   
        print(serializer.errors)
        return render(request, 'login.html', {'errors': 'Credenciais inválidas. Tente novamente.'})
    
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