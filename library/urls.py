from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.book import *


urlpatterns = [
    path(r'', ListBookView.as_view(),  name="books-list" ),
    path(r'create/', CreateBookView.as_view(),  name="create-book" ),
    path(r'delete/<str:pk>', DeleteBookView.as_view(),  name="delete-book" ),
    path(r'update/<str:pk>', EditBookView.as_view(),  name="update-book" )
]
