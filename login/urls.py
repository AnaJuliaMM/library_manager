from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.login import LoginView

router = DefaultRouter()
router.register(r'', LoginView)

urlpatterns = [
    path('', include(router.urls)),
]
