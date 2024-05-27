from rest_framework import serializers
from ..models.book import Book

class Book(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields =  '__all__'