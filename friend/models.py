from django.db import models

# Create your models here.

class Friends(models.Model):
    id = models.IntegerField(verbose_name = 'id', primary_key=True)
    follow_user_id = models.IntegerField(verbose_name = 'follow_user_id')
    followed_user_id = models.IntegerField(verbose_name = 'followed_user_id')
    created_at = models.DateTimeField(verbose_name = 'created_at')
    updated_at = models.DateTimeField(verbose_name = 'updated_at')

    class Meta(object):
        verbose_name_plural = 'Friends'