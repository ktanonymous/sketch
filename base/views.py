from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User, Friend, Event, Information, AdjustingSchedule
from .serializers import UserSerializer, RetrieveUserSerializer


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


class GetFriendListView(generics.ListAPIView):
    permission_classes = (
        AllowAny,  # TODO: 本当はAllowAny良くないので後で直すべし
    )
    serializer_class = UserSerializer

    def get_queryset(self):
        return super().get_queryset()
