from django.forms import ValidationError
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from django.http.response import HttpResponse
from django.contrib import messages


from ..models.book import BookModel
from ..serializers.book import BookSerializer
from ..forms.book import BookForm
from ..repository import BookRepository

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ListBookView(TemplateView):
    template_name = 'books.html'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def dispatch(self, request, *args, **kwargs):
        self.is_authenticated = False
        for authenticator in self.authentication_classes:
            try:
                self.user, _ = authenticator().authenticate(request)
                if self.user is not None:
                    request.user = self.user
                    self.is_authenticated = True
                    break
            except:
                pass
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_authenticated'] = self.is_authenticated
        try:
            books = BookRepository().get_all_books()
            serialized_books = BookSerializer(books, many=True)
            context['books'] = serialized_books.data

            title = self.request.GET.get('title')

            if title:
                filters = {}
                filters['title__icontains'] = title
                books = BookRepository().filter_books(filters)
                serializer = BookSerializer(books, many=True)
                context['books'] = serializer.data

        except ValidationError as e:
            context['errors'] = e
        except Exception as e:
            context['errors'] = e
        return context


class CreateBookView(TemplateView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    template_name = 'createBook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookForm()
        return context

    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            serializer = BookSerializer(data=data)
            if  serializer.is_valid():
                BookRepository().create_book(**data)
                return redirect('books-list')
            else:
                context = self.get_context_data(**kwargs)
                context['form'] = form
                context['serializer_errors'] = serializer.errors
                return self.render_to_response(context)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['errors'] = form.errors 
        return self.render_to_response(context)


class DeleteBookView(TemplateView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    template_name = 'verifyDelete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = kwargs.get('pk')
        try:
            book = get_object_or_404(BookModel, pk=book_id)
            serializer = BookSerializer(book)
            context['book'] = serializer.data
        except Http404:
            context['errors'] = 'O livro solicitado não existe.'
        except ValidationError as e:
            context['serializer_errors'] = e
        return context

    def post(self, request, *args, **kwargs):
        book_id = kwargs.get('pk')
        repository = BookRepository()
        success = repository.delete_book(book_id)
        if success:
            return redirect('books-list')
        return redirect('books-list')


class EditBookView(TemplateView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    template_name = 'updateBook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = kwargs.get('pk')
        try:
            book = get_object_or_404(BookModel, pk=book_id)
            serializer = BookSerializer(book)
            form = BookForm(instance=book)
            context['book'] = serializer.data
            context['form'] = form
        except Http404:
            context['errors'] = 'O livro solicitado não existe.'
        except ValidationError as e:
            context['serializer_errors'] = e
        return context
    

    def post(self, request, *args, **kwargs):
        book_id = kwargs.get('pk')
        repository = BookRepository()
        book = repository.get_book_by_id(book_id)
        if book:
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('books-list')
                except ValidationError as e:
                    context = self.get_context_data(**kwargs)
                    context['serializer_errors'] = e
                    context['form'] = form
                    return self.render_to_response(context)
        return redirect('books-list')
 