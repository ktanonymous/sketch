from django.shortcuts import render
from rest_framework import status, generics

from .models import User, Friend, Event, Information, AdjustingSchedule
from .serializer import UserSerializer, FriendSerializer, EventSerializer, AdjustingScheduleSerializer, InformationSerializer


class FriendAPI(generics.CreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer