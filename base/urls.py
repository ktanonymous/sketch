from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from .views import (
    AdjustingEventView,
    FriendFollowView,
    FriendsListView,
    IndexView,
    ProposeEventView,
    FilterProposeFriendsView,
)

app_name = 'base'
urlpatterns = [
    path('adjusting/<int:pk>', AdjustingEventView.as_view(), name='adjusting'),
    path('follow/', FriendFollowView.as_view(), name='follow'),
    path('friends/', FriendsListView.as_view(), name='friends'),
    path('index/', IndexView.as_view(), name='index'),
    path('propose/', ProposeEventView.as_view(), name='propose'),
    path('propose/filter/<int:pk>', FilterProposeFriendsView.as_view(), name='propose'),
]
