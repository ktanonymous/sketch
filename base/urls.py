from django.contrib import admin
from django.urls import path, include

from .views import (
    UserRegistrationView,
    GetUserView,
    RetriveUserView,
)


urlpatterns = [
    path('user/registration', UserRegistrationView.as_view()),
    path('user/get', GetUserView.as_view()),
    path('user/retrieve/<int:pk>', RetriveUserView.as_view()),
]
