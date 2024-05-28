from rest_framework import viewsets
from django.shortcuts import render
from ..models.user import UserModel
from ..serializers.user import UserSerializer

class UserViewSet (viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer