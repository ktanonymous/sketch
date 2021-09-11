from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from .views import (
    AdjustingEventView,
    FriendFollowView,
    FriendsListView,
    IndexView,
    ProposeEventView,
    FilterFriendsView,
)

app_name = 'base'
urlpatterns = [
    path('adjusting/<int:pk>', AdjustingEventView.as_view(), name='adjusting'),
    path('follow/', FriendFollowView.as_view(), name='follow'),
    path('friends/', FriendsListView.as_view(), name='friends'),
    path('index/', IndexView.as_view(), name='index'),
    path('propose/', ProposeEventView.as_view(), name='propose'),
    # TODO: 上手いやり方を模索、ヘッダーに含めたりする？→クエリストリング(/?&~~)
    path('propose/filter', FilterFriendsView.as_view(), name='propose_filter'),
]
