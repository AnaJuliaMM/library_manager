from django.forms import ValidationError
from django.contrib.auth import login,authenticate
from django.shortcuts import redirect,render,get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from .authentication import *
from typing import Any
from django.http.response import HttpResponse
from django.http import Http404, HttpResponseForbidden,HttpRequest


from .repository import CustomUserRepository
from .serializers import CustomUserSerializer
from .forms import UserForm

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token = generate_token(user)
            response = redirect('books-list')
            response.set_cookie('jwt', token)
            return response
        return render(request, 'login.html', {'errors': 'Credenciais inválidas. Tente novamente.'})

class LogoutView(View):
    def get(self, request):
        response = redirect('books-list')
        response.delete_cookie('jwt')
        return response
    
class ListUserView(TemplateView):
    template_name = 'users.html'
    is_authenticated = False
    user = None

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        """Função que intercepta a requisição

        Args:
            request (HttpRequest): Rrequisição

        Returns:
            HttpResponse: redirecionamento
        """
        try:
            token = request.COOKIES.get('jwt')
            error_code, _ = verify_token(token)

            if error_code == 0:
                user = get_authenticated_user(token)
                self.user = user
                self.is_authenticated = True
            else:
                return HttpResponseForbidden('Você não está autenticado!')
        except Exception as e:
            return self.get(request)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_authenticated'] = self.is_authenticated
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
    # is_authenticated = False
    # user = None

    # def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     """Função que intercepta a requisição

    #     Args:
    #         request (HttpRequest): Rrequisição

    #     Returns:
    #         HttpResponse: redirecionamento
    #     """
    #     try:
    #         token = request.COOKIES.get('jwt')
    #         error_code, _ = verify_token(token)
            

    #         if error_code == 0:
    #             user = get_authenticated_user(token)
    #             self.user = user
    #             self.is_authenticated = True
    #         else:
    #             return HttpResponseForbidden('Você não está autenticado!')
    #     except Exception as e:
    #         return self.get(request)
    #     return super().dispatch(request, *args, **kwargs)

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

class DeleteUserView(TemplateView):
    template_name = 'verifyDeleteUser.html'
    is_authenticated = False
    user = None

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        """Função que intercepta a requisição

        Args:
            request (HttpRequest): Rrequisição

        Returns:
            HttpResponse: redirecionamento
        """
        try:
            token = request.COOKIES.get('jwt')
            error_code, _ = verify_token(token)
            

            if error_code == 0:
                user = get_authenticated_user(token)
                self.user = user
                self.is_authenticated = True
            else:
                return HttpResponseForbidden('Você não está autenticado!')
        except Exception as e:
            return self.get(request)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = kwargs.get('pk')
        try:
            user = get_object_or_404(CustomUser, pk=user_id)
            serializer = CustomUserSerializer(user)
            context['users'] = serializer.data
        except Http404:
            context['errors'] = 'O usuário solicitado não existe.'
        except ValidationError as e:
            context['serializer_errors'] = e
        return context

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        repository = CustomUserRepository()
        user = repository.filter_user({"id": user_id})
        success = repository.delete_user(user)
        if success:
            return redirect('users-list')
        return redirect('users-list')