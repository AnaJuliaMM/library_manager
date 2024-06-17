
from django.urls import path, include
from .views import *

urlpatterns = [
    path(r'', ListUserView.as_view(),  name="users-list" ),
    path(r'create/', CreateUserView.as_view(),  name="create-user" ),
    path('login/', LoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path(r'delete/<str:pk>', DeleteUserView.as_view(),  name="delete-user" ),
]
