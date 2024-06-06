from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.user_admin import UserAdminViewSet

router = DefaultRouter()
router.register(r'', UserAdminViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
