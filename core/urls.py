from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views
from user.views import CustomLoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),
    path('users/', include('user.urls')),
    path('api_token_auth/', authtoken_views.obtain_auth_token),
    path('accounts/', include('django.contrib.auth.urls')),
]