from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.book import *

router = DefaultRouter()
router.register(r'books', GenericBookView, basename="books")
router.register(r'create', CreateBookView, basename="book")


urlpatterns = [
    path('', include(router.urls)),
    path(r'delete/<str:pk>', DeleteBookView.as_view(),  name="delete-book" )
]
