from django.urls import path
from home.views import index, Person, login, UserAPI



urlpatterns = [
    path('index/', index),
    path('user/', Person),
    path('login/', login),
    path('users/', UserAPI.as_view)
]
