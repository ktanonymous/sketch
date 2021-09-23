"""テーブルを表現するためのモデルを定義する
モデル定義を変更した場合は、マイグレーションの履歴及びデータベースを作り直す必要がある
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator

# モデルを利用するときには、<モデルクラス>.<モデルマネージャ>.get のようにしてアクセスする
# デフォルトのモデルマネージャから変更を加えたい時に、マネージャを設定する
from .managers import UserManager


# AbstractBaseUser は username 以外でのユーザー認証をするために継承
# AbstractBaseUser を利用する際は、BaseUserManager を継承したカスタムマネージャが必要(今回は、UserManager)
# AbstractBaseUser は、権限周りの機能を持たないため、Django の権限モデルを全て含む PermissionsMixin を継承する必要がある
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name='ユーザー名', max_length=10, validators=[UnicodeUsernameValidator])
    email = models.EmailField(verbose_name='メールアドレス', max_length=255, unique=True)
    password = models.CharField(verbose_name='パスワード', max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # モデルマネージャを表すのが objects （名前は Django のデフォルトで決まっている）
    objects = UserManager()

    # 識別子をメアドにする
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    class Meta(object):
        verbose_name_plural = 'Users'
        db_table = 'users'

    def __str__(self):
        return self.username


class Friend(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    follow_user = models.ForeignKey(User, related_name='follow_user', verbose_name='follow_user', on_delete=models.CASCADE, db_column='follow_user_id')
    followed_user = models.ForeignKey(User, related_name='followed_user', verbose_name='followed_user', on_delete=models.CASCADE, db_column='followed_user_id')

    class Meta(object):
        verbose_name_plural = 'Friends'
        db_table = 'friends'

    def __str__(self):
        return str(self.follow_user.username) + ' - ' + str(self.followed_user.username)


class AdjustingEvent(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    # 日程調整の提案者
    proposer = models.ForeignKey(User, verbose_name='proposer', related_name='proposer', on_delete=models.CASCADE, db_column='proposer_id')
    name = models.CharField(verbose_name='イベント名', max_length=30)
    # dateX_start: X 番目の候補日の開始日時
    # dateX_end: X 番目の候補日の終了日時
    date1_start = models.DateTimeField(verbose_name='date1_start', null=True, blank=True)
    date1_end = models.DateTimeField(verbose_name='date1_end', null=True, blank=True)
    date2_start = models.DateTimeField(verbose_name='date2_start', null=True, blank=True)
    date2_end = models.DateTimeField(verbose_name='date2_end', null=True, blank=True)
    date3_start = models.DateTimeField(verbose_name='date3_start', null=True, blank=True)
    date3_end = models.DateTimeField(verbose_name='date3_end', null=True, blank=True)
    date4_start = models.DateTimeField(verbose_name='date4_start', null=True, blank=True)
    date4_end = models.DateTimeField(verbose_name='date4_end', null=True, blank=True)
    date5_start = models.DateTimeField(verbose_name='date5_start', null=True, blank=True)
    date5_end = models.DateTimeField(verbose_name='date5_end', null=True, blank=True)
    # frinedX: 日程調整に招待されたユーザー
    friend1 = models.ForeignKey(User, verbose_name='友達1', related_name='friend1', on_delete=models.CASCADE, db_column='friend1_id')
    friend2 = models.ForeignKey(User, verbose_name='友達2', related_name='friend2', on_delete=models.CASCADE, db_column='friend2_id', null=True, blank=True)
    friend3 = models.ForeignKey(User, verbose_name='友達3', related_name='friend3', on_delete=models.CASCADE, db_column='friend3_id', null=True, blank=True)
    # 日程調整を受け取ったユーザーが何番目のユーザーであるかを確かめる数字
    rest_friends_num = models.IntegerField(verbose_name='rest_friends_num', blank=True)

    class Meta(object):
        verbose_name_plural = 'AdjustingEvents'
        db_table = 'adjusting_events'

    def __str__(self):
        return 'イベント名：' + self.name


class Event(models.Model):
    """日程調整が完了したイベントを管理するモデル"""
    id = models.AutoField(verbose_name='id', primary_key=True)
    name = models.CharField(verbose_name='イベント名', max_length=30)
    date_start = models.DateTimeField(verbose_name='開始日時')
    date_end = models.DateTimeField(verbose_name='終了日時')
    participant = models.ForeignKey(User, verbose_name='participant_id', on_delete=models.CASCADE, db_column='participant_id')

    class Meta(object):
        verbose_name_plural = 'Events'
        db_table = 'events'

    def __str__(self):
        return self.name + ' (user_id: ' + str(self.participant) + ' )'


class Information(models.Model):
    """インデックスページに表示するお知らせを管理するモデル"""
    id = models.AutoField(verbose_name='id', primary_key=True)
    event_name = models.CharField(verbose_name='イベント名', max_length=255)
    receiver = models.ForeignKey(User, verbose_name='receiver_id', related_name='receiver', on_delete=models.CASCADE, db_column='receiver_id')
    sender = models.ForeignKey(User, verbose_name='sender_id', related_name='sender', on_delete=models.CASCADE, db_column='sender_id')
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True)
    adjusting_event = models.ForeignKey(AdjustingEvent, verbose_name='adjusting_event_id', blank=True, null=True, on_delete=models.CASCADE, db_column='adjusting_event_id')
    event = models.ForeignKey(Event, verbose_name='event_id', blank=True, null=True, on_delete=models.CASCADE, db_column='event_id')

    class Meta(object):
        verbose_name_plural = 'Informations'
        db_table = 'informations'

    def __str__(self):
        return self.event_name + '(user_id: ' + str(self.receiver) + ')'
