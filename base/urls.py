from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import (
    IndexView,
    FriendsListView,
    FriendApplicationView
)

app_name = 'base'
urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('friends/', FriendsListView.as_view(), name='friends'),
    path(
        'friends/application',
        FriendApplicationView.as_view(),
        name='friend_application'
    ),
]
