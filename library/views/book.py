from rest_framework import viewsets
from django.shortcuts import render

from ..models import BookModel
from ..serializers import BookSerializer

class BookViewSet (viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer