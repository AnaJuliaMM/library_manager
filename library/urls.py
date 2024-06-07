from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.book import *

router = DefaultRouter()
router.register(r'books', ListBookView, basename="books")
router.register(r'create', CreateBookView, basename="book")

urlpatterns = [
    path('', include(router.urls)),
]
