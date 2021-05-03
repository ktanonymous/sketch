from django.contrib import admin
from django.urls import path, include

from .views import (
    UserRegistrationView,
    GetUserView,
)


urlpatterns = [
    path('user/registration', UserRegistrationView.as_view()),
    path('user/get', GetUserView.as_view()),
]
