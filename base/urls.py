from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import (
    IndexView,
    AdjustingScheduleView,
    FriendFollowView,
    FriendsListView,
    ProposeScheduleView,
)

app_name = 'base'
urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('propose/', ProposeScheduleView.as_view(), name='propose'),
    path('follow/', FriendFollowView.as_view(), name='follow'),
    path('friends/', FriendsListView.as_view(), name='friends'),
    # path('adjusting/', AdjustingScheduleView.as_view(), name='adjusting'),
    path('adjusting/<int:pk>', AdjustingScheduleView.as_view(), name='adjusting'),
]
