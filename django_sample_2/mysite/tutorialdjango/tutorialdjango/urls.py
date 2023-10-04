from django.contrib import admin
from django.urls import path
from main.views import index, about, contact, login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('contact/', contact),
    path('accounts/login', login),
    path('accounts/logout', logout),
]