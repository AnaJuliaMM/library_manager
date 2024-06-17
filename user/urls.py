
from django.urls import path, include
from .views import *

urlpatterns = [
    path(r'', ListUserView.as_view(),  name="users-list" ),
    path(r'create/', CreateUserView.as_view(),  name="create-user" ),
    # path(r'delete/<str:pk>', DeleteBookView.as_view(),  name="delete-book" ),
    # path(r'update/<str:pk>', EditBookView.as_view(),  name="update-book" )
]
