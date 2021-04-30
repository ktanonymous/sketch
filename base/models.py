from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator

    # id = models.AutoField(verbose_name='ユーザーID', primary_key=True)
    username = models.CharField(verbose_name='ユーザー名', max_length=10, validators=[username_validator])
    email = models.EmailField(verbose_name='メールアドレス', max_length=255, unique=True)
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
    follow_user_id = models.ForeignKey(User, related_name='follow_userid', verbose_name='follow_user_id', blank=True, on_delete=models.CASCADE, db_column='follow_user_id')
    followed_user_id = models.ForeignKey(User, related_name='followed_userid', verbose_name='followed_user_id', blank=True, on_delete=models.CASCADE, db_column='followed_user_id')

    class Meta(object):
        verbose_name_plural = 'Friends'

    def __str__(self):
        return str(self.follow_user_id.username) + ' - ' + str(self.followed_user_id.username)