from rest_framework.serializers import ModelSerializer
from .models import User, Friend, Event


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
        )

    def create(self, validated_data):
        user = User()
        user.email = validated_data['email']
        user.username = validated_data['username']
        user.set_password(validated_data['password'])
        user.save()
        return user


class FriendSerializer(ModelSerializer):
    class Meta:
        model = Friend
        fields = (
            'id',
            'follow_user_id',
            # 'followed_user_id',
        )


class RetrieveUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'name',
            'date_start',
            'date_end',
        )
