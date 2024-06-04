from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.book import BookViewSet

router = DefaultRouter()
router.register(r'', BookViewSet, basename="books")

urlpatterns = [
    path('', include(router.urls)),
]
