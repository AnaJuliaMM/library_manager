from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import TemplateView
from django.views import View

from ..models.book import BookModel
from ..serializers.book import BookSerializer
from ..forms.book import BookForm
from ..repository import BookRepository


class ListBookView(TemplateView):
    template_name = 'books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = BookRepository().get_all_books()
        serialized_books = BookSerializer(books, many=True)
        context['books'] = serialized_books.data
        return context


class CreateBookView(TemplateView):
    template_name = 'createBook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookForm()
        return context

    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BookRepository().create_book(**data)
            return redirect('books-list')
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            context['errors'] = form.errors
            return self.render_to_response(context)


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
            return redirect('books-list')
        return redirect('books-list')
        # return HttpResponse(status=405)

class EditBookView(TemplateView):
    template_name = 'updateBook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = kwargs.get('pk')
        book = get_object_or_404(BookModel, pk=book_id)

        serializer = BookSerializer(book)
        serialized_data = serializer.data
        print(serialized_data)
        form = BookForm(instance=book)
        print(form)
        context['book'] = serialized_data  
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        book_id = kwargs.get('pk')
        repository = BookRepository()
        book = repository.get_book_by_id(book_id)
        if book:
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                return redirect('books-list')
        return redirect('books-list')
        # return HttpResponse(status=405)
 