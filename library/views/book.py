from rest_framework import viewsets
from django.shortcuts import render, redirect
from ..models.book import BookModel
from ..serializers.book import BookSerializer
from ..forms.create_book import BookForm

class ListBookView (viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        books = self.queryset
        return render(request, 'books.html', {'books': books})

class CreateBookView (viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    http_method_names = ['get', 'post']

    def list(self, request, *args, **kwargs):
        form = BookForm()
        return render(request, 'createBook.html', { "form": form})
    
    def create(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
          
            form.save()
            return redirect('books-list')
        errors = form.errors
        print(errors)
        return render(request, 'createBook.html', {'form': form, 'errors': errors})
