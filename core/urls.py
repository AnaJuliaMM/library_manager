from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('library.urls')),
    path('users/', include('user.urls')),
    path('user_admin/', include('user_admin.urls')),
    path('login/', include('login.urls')),
    
]
