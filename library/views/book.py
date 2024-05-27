from rest_framework import viewsets
from django.shortcuts import render
from ..models.book import BookModel
from ..serializers.book import BookSerializer

class BookViewSet (viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer