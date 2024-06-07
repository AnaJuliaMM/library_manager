from django import forms
from ..models.book import BookModel

class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['title', 'author', 'publisher', 'gender', 'pages', 'publish_date']
        labels = {
                    'title': 'Título',
                    'author': 'Autor',
                    'publisher': 'Editora',
                    'gender': 'Gênero',
                    'pages': 'Número de Páginas',
                    'publish_date': 'Data de Publicação',
                }