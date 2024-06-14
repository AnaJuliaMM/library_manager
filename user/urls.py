from django.urls import path
from .views.user import UserLoginPage, UserLoginView

urlpatterns = [
    path('', UserLoginPage.as_view({'get': 'list'}), name='login-page'),  # Renderiza a página de login
    path('user/', UserLoginView.as_view({'post': 'create'}), name='user-login'),  # Endpoint de login da API
]
