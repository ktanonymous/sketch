from django.contrib import admin
from django.urls import path

from .views import FriendAPI

urlpatterns = [
    path('api/v1/friend', FriendAPI.as_view()),
]
