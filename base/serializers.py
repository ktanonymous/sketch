from rest_framework.serializers import ModelSerializer
from .models import User, Friend, Event, AdjustingSchedule, Information

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


class RetrieveUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )

class FriendSerializer(ModelSerializer):
    class Meta:
        model = Friend
        fields = (
            'follow_user_id',
            'followed_user_id',
        )

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'name',
            'date_start',
            'date_end',
            'user_id'
        )

class AdjustingScheduleSerializer(ModelSerializer):
    class Meta:
        model = AdjustingSchedule
        fields = (
            'id',
            'master_user_id',
            'name',
            'date1_start',
            'date1_end',
            'date2_start',
            'date2_end',
            'date3_end',
            'date3_start',
            'date4_end',
            'date4_end',
            'date5_start',
            'date5_end',
            'friend1',
            'friend2',
            'friend3',
            'current_user_num',
        )

class InformationSerializer(ModelSerializer):
    class Meta:
        model = Information
        fields = (
            'id',
            'message',
            'user_id',
            'created_at',
            'adjsuting_schedules_id',
            'events_id',
        )