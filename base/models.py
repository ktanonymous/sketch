from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator

    username = models.CharField(
        verbose_name='ユーザー名', max_length=10, validators=[username_validator])
    email = models.EmailField(verbose_name='メールアドレス',
                              max_length=255, unique=True)
    password = models.CharField(verbose_name='パスワード', max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta(object):
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Friend(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    follow_user_id = models.ForeignKey(User, related_name='follow_userid',
                                       verbose_name='follow_user_id', on_delete=models.CASCADE, db_column='follow_user_id')
    followed_user_id = models.ForeignKey(User, related_name='followed_userid',
                                         verbose_name='followed_user_id', on_delete=models.CASCADE, db_column='followed_user_id')

    class Meta(object):
        verbose_name_plural = 'Friends'

    def __str__(self):
        return str(self.follow_user_id.username) + ' - ' + str(self.followed_user_id.username)


class AdjustingSchedule(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    master_user_id = models.ForeignKey(User, verbose_name='master_user_id',
                                       related_name='master_user_id', on_delete=models.CASCADE, db_column='master_user_id')
    name = models.CharField(verbose_name='イベント名', max_length=30)
    date1_start = models.DateTimeField(
        verbose_name='date1_start', null=True, blank=True)
    date1_end = models.DateTimeField(
        verbose_name='date1_end', null=True, blank=True)
    date2_start = models.DateTimeField(
        verbose_name='date2_start', null=True, blank=True)
    date2_end = models.DateTimeField(
        verbose_name='date2_end', null=True, blank=True)
    date3_start = models.DateTimeField(
        verbose_name='date3_start', null=True, blank=True)
    date3_end = models.DateTimeField(
        verbose_name='date3_end', null=True, blank=True)
    date4_start = models.DateTimeField(
        verbose_name='date4_start', null=True, blank=True)
    date4_end = models.DateTimeField(
        verbose_name='date4_end', null=True, blank=True)
    date5_start = models.DateTimeField(
        verbose_name='date5_start', null=True, blank=True)
    date5_end = models.DateTimeField(
        verbose_name='date5_end', null=True, blank=True)
    friend1 = models.ForeignKey(
        User, verbose_name='友達1', related_name='friend1', on_delete=models.CASCADE, db_column='friend1')
    friend2 = models.ForeignKey(User, verbose_name='友達2', related_name='friend2',
                                on_delete=models.CASCADE, db_column='friend2', null=True, blank=True)
    friend3 = models.ForeignKey(User, verbose_name='友達3', related_name='friend3',
                                on_delete=models.CASCADE, db_column='friend3', null=True, blank=True)
    current_user_num = models.IntegerField(
        verbose_name='current_user_num', blank=True)

    class Meta(object):
        verbose_name_plural = 'AdjustingSchedules'

    def __str__(self):
        return 'イベント名：' + self.name


class Event(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    name = models.CharField(verbose_name='イベント名', max_length=30)
    date_start = models.DateTimeField(verbose_name='開始日時')
    date_end = models.DateTimeField(verbose_name='終了日時')
    user_id = models.IntegerField(verbose_name='user_id')

    class Meta(object):
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.name + ' (user_id: ' + str(self.user_id) + ' )'


class Information(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    message = models.CharField(verbose_name='メッセージ', max_length=255)
    user_id = models.ForeignKey(
        User, verbose_name='user_id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        verbose_name='created_at', auto_now_add=True)
    adjusting_schedules_id = models.ForeignKey(
        AdjustingSchedule, verbose_name='adjusting_schedules_id', blank=True, null=True, on_delete=models.CASCADE)
    events_id = models.ForeignKey(
        Event, verbose_name='events_id', blank=True, null=True, on_delete=models.CASCADE)

    class Meta(object):
        verbose_name_plural = 'Informations'

    def __str__(self):
        return self.message
