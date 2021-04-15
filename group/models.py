from django.db import models
from base.models import Users
from django.utils import timezone


class Groups(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    name = models.CharField(verbose_name='グループ名', max_length=20)
    icon_path = models.CharField(verbose_name='icon_path', max_length=255)
    calender_path = models.CharField(verbose_name='calender_path', max_length=255)
    created_at = models.DateTimeField(verbose_name='created_at', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='updated_at', default=timezone.now)

    user_id = models.ManyToManyField(Users, verbose_name='user_id', db_table='Users_Groups')

    class Meta(object):
        verbose_name_plural = 'Groups'

    def __str__(self):
        return self.name

# class Users_Groups(models.Model):
#     id = models.AutoField(verbose_name='id', primary_key=True)
#     user_id = models.ForeignKey(Users, verbose_name='user_id', db_column='user_id', on_delete=models.CASCADE)
#     group_id = models.ForeignKey(Groups, verbose_name='group_id', db_column='group_id', on_delete=models.CASCADE)

#     class Meta(object):
#         verbose_name_plural = ''
