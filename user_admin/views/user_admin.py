from rest_framework import viewsets
from django.shortcuts import render
from ..models.user_admin import UserAdminModel
from ..serializers.user_admin import UserAdminSerializer

class UserAdminViewSet (viewsets.ModelViewSet):
    queryset = UserAdminModel.objects.all()
    serializer_class = UserAdminSerializer