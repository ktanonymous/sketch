from rest_framework import serializers
from .models import User
from ..friend.models import Friend

class UsersSerializers(serializers.ModelSerializers):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            # 'mailaddress',
            # 'is_staff',
        )

class FriendsSerializers(serializers.ModelSerializers):
    class Meta:
        model = Friend
        fields = (
            'id',
            'follow_user_id',
            # 'followed_user_id',
        )