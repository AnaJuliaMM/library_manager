from django import forms
from ..models.book import BookModel

class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['title', 'author', 'publisher', 'gender', 'pages', 'publish_date']