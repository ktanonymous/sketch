from django.db import models
from base.models import User
from django.utils import timezone
# Create your models here.

class Friend(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    follow_user_id = models.ForeignKey(User, related_name='follow_userid', verbose_name='follow_user_id', blank=True, on_delete=models.CASCADE, db_column='follow_user_id')
    followed_user_id = models.ForeignKey(User, related_name='followed_userid', verbose_name='followed_user_id', blank=True, on_delete=models.CASCADE, db_column='followed_user_id')

    class Meta(object):
        verbose_name_plural = 'Friends'

    def __str__(self):
        return str(self.follow_user_id.username) + ' - ' + str(self.followed_user_id.username)
