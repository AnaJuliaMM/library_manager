from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render, redirect
from ..models.book import BookModel
from ..serializers.book import BookSerializer
from ..forms.create_book import BookForm
from ..repository import BookRepository

from django.urls import reverse_lazy
from django.views.generic import DeleteView


class GenericBookView(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    http_method_names = ['get', 'delete']

    def list(self, request, *args, **kwargs):
        books = BookRepository().get_all_books()
        serialized_books = self.serializer_class(books, many=True)
        return render(request, 'books.html', {"books": serialized_books.data })
        
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

def delete_instance(request, id):
    if request.method == 'GET':
        BookRepository().delete_book(id)
        return redirect('books-list')
    return HttpResponse(status=405)

class DeleteView(DeleteView):
    model = BookModel
    template_name = 'verifyDelete.html'
    success_url = reverse_lazy('books-list')  
    print("aa")