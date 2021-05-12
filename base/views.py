from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User, Friend, Event, Information, AdjustingSchedule
from .serializers import (
    UserSerializer,
    RetrieveUserSerializer,
    FriendSerializer,
    EventSerializer,
    AdjustingScheduleSerializer,
    InformationSerializer,
)
from django.views import generic


class UserRegistrationView(generics.CreateAPIView):
    permission_classes = (
        AllowAny,
    )
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetUserView(APIView):
    permission_classes = (
        AllowAny,  # TODO: 本当はAllowAny良くないので後で直すべし
    )

    def get(self, request):
        id = request.data['id']
        user = User.objects.get(pk=id)
        data = {'username': user.username, 'email': user.email}
        return Response(data, status=status.HTTP_200_OK)


class RetriveUserView(generics.RetrieveAPIView):
    permission_classes = (
        AllowAny,  # TODO: 本当はAllowAny良くないので後で直すべし
    )
    queryset = User.objects.all()
    serializer_class = RetrieveUserSerializer


class CreateFriendView(generics.CreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class GetFriendListView(generics.ListAPIView):
    permission_classes = (
        AllowAny,  # TODO: 本当はAllowAny良くないので後で直すべし
    )
    serializer_class = FriendSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = Friend.objects.filter(followed_user_id=id)
        return queryset


class IndexView(generic.ListView):
    model = Information
    template_name = 'index.html'

    def get_queryset(self):
        informations = Information.objects.filter(user_id=2)
        return informations


class WelcomeView(generic.TemplateView):
    template_name = 'welcome.html'


class FriendsListView(generic.ListView):
    model = Friend
    template_name = 'friends_list.html'
    paginate_by = 3

    # def get_queryset(self, request):
    #     id = request.data['id']
    #     # ログインユーザーの情報を使いたい場合にはself.request.userみたいな感じにやる
    #     friends = Friend.objects.filter(followed_user_id=id)
    #     return friends

    def get_queryset(self):
        # ログインユーザーの情報を使いたい場合にはself.request.userみたいな感じにやる
        friends = Friend.objects.filter(followed_user_id=2)
        return friends


class FriendApplicationView(generic.TemplateView):
    template_name = 'friend_application.html'
