from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import (
    UserRegistrationView,
    GetUserView,
    RetriveUserView,
    CreateFriendView,
    GetFriendListView,
    IndexView,
    FriendsListView,
    FriendApplicationView
)

app_name = 'base'
urlpatterns = [
    path('user/registration', UserRegistrationView.as_view()),
    path('user/get', GetUserView.as_view()),
    path('user/retrieve/<int:pk>', RetriveUserView.as_view()),
    path('friend/create', CreateFriendView.as_view()),
    path('friend/list/<int:pk>', GetFriendListView.as_view()),
    path('index/', IndexView.as_view(), name='index'),
    path('friends/', FriendsListView.as_view(), name='friends'),
    path(
        'friends/application',
        FriendApplicationView.as_view(),
        name='friend_application'
    ),
]
