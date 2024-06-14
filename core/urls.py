from django.contrib import admin
from django.urls import path, include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('library.urls')),
    path('user_admin/', include('user_admin.urls')),
    path('login/', include('user.urls')), 
]
