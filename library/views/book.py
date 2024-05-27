from rest_framework import viewsets
from django.shortcuts import render

from ..models import Book
from ..serializers import Book

class Book (viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Book