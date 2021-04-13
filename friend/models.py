from django.db import models
from base.models import Users
from django.utils import timezone
# Create your models here.

class Friends(models.Model):
    id = models.AutoField(verbose_name = 'id', primary_key=True)
    follow_user_id = models.ForeignKey(Users, related_name = 'follow_userid', verbose_name = 'follow_user_id', blank = True, on_delete = models.CASCADE)
    followed_user_id = models.ForeignKey(Users, related_name = 'followed_userid', verbose_name = 'followed_user_id', blank = True, on_delete = models.CASCADE)
    created_at = models.DateTimeField(verbose_name = 'created_at', default = timezone.now)
    updated_at = models.DateTimeField(verbose_name = 'updated_at', default = timezone.now)

    class Meta(object):
        verbose_name_plural = 'Friends'

    def __str__(self):
        return str(self.follow_user_id.id) +'-'+ str(self.followed_user_id.id)