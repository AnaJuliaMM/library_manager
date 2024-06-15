from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views
from user.views.user import CustomLoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('library.urls')),
    path('api_token_auth/', authtoken_views.obtain_auth_token),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
]
