from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('library.urls')),
    path('api_token_auth/', authtoken_views.obtain_auth_token),
    path('accounts/', include('django.contrib.auth.urls')),
]
