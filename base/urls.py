from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import (
    UserRegistrationView,
    GetUserView,
    RetriveUserView,
    CreateFriendView,
    GetFriendListView,
    HomeView,
    WelcomeView,
)


urlpatterns = [
    path('user/registration', UserRegistrationView.as_view()),
    path('user/get', GetUserView.as_view()),
    path('user/retrieve/<int:pk>', RetriveUserView.as_view()),
    path('friend/create', CreateFriendView.as_view()),
    path('friend/list/<int:pk>', GetFriendListView.as_view()),
    path('home/', HomeView.as_view(), name='home'),
    path('welcome/', WelcomeView.as_view(), name='welcome'),
]
