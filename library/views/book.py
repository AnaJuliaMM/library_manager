from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render, redirect,get_object_or_404
from ..models.book import BookModel
from ..serializers.book import BookSerializer
from ..forms.create_book import BookForm
from ..repository import BookRepository

from django.views.generic import TemplateView


# Mudar para função
class GenericBookView(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    http_method_names = ['get', 'delete']

    def list(self, request, *args, **kwargs):
        books = BookRepository().get_all_books()
        serialized_books = self.serializer_class(books, many=True)
        return render(request, 'books.html', {"books": serialized_books.data })

# Mudar para função        
class CreateBookView(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    http_method_names = ['get', 'post']

    def list(self, request, *args, **kwargs):
        form = BookForm()
        return render(request, 'createBook.html', {"form": form})
    
    def create(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BookRepository().create_book(**data)
            return redirect('books-list')
        errors = form.errors
        return render(request, 'createBook.html', {'form': form, 'errors': errors})


class DeleteBookView(TemplateView):
    template_name = 'verifyDelete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = kwargs.get('pk')
        book = get_object_or_404(BookModel, pk=book_id)
        context['book'] = book
        return context

    def post(self, request, *args, **kwargs):
        book_id = kwargs.get('pk')
        repository = BookRepository()
        success = repository.delete_book(book_id)
        if success:
            return redirect('list_books')
        return redirect('list_books')
        # return HttpResponse(status=405)
