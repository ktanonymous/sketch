from django.db import models

class Users(models.Model):
    id = models.IntegerField(verbose_name = 'ユーザーID', primary_key = True)
    first_name = models.CharField(verbose_name = '名前', max_length = 30)
    first_name_pronunciation = models.CharField(verbose_name = 'なまえ', max_length = 30, blank = True, null = True)
    last_name = models.CharField(verbose_name = '名字', max_length = 30)
    last_name_pronunciation = models.CharField(verbose_name = 'みょうじ', max_length = 30, blank = True, null = True)
    nickname = models.CharField(verbose_name = '表示名', max_length = 10, blank = True, null = True)
    age = models.IntegerField(verbose_name = '年齢', blank = True, null = True)
    sex = models.BinaryField(verbose_name = '性別', blank = True, null = True)
    mail_address = models.CharField(verbose_name = 'メールアドレス', max_length = 255)
    password = models.CharField(verbose_name = 'パスワード', max_length = 255)
    icon_path = models.CharField(verbose_name = 'icon_path', max_length = 255, blank = True, null = True)
    calendar_path = models.CharField(verbose_name = 'calendar_path', max_length = 255, blank = True, null = True)
    created_at = models.DateTimeField(verbose_name = '作成日時')
    updated_at = models.DateTimeField(verbose_name = '更新日時')

    class Meta(object):
        verbose_name_plural = 'Users'

class ResponseLogs(models.Model):
    id = models.IntegerField(verbose_name = 'id', primary_key = True)
    user_id = models.ForeignKey(Users, verbose_name = 'user_ID', blank = True, null = True, on_delete = models.SET_NULL)
    session_id = models.CharField(verbose_name = 'session_id', max_length = 255)
    http_method = models.CharField(verbose_name = 'http_method', max_length = 20)
    url = models.CharField(verbose_name = 'url', max_length = 255)
    status_code = models.IntegerField(verbose_name = 'calendar_path')
    text_phrase = models.CharField(verbose_name = 'text_phrase', max_length = 255)
    created_at = models.DateTimeField(verbose_name = 'created_at')

    class Meta(object):
        verbose_name_plural = 'Response Logs'

class RequestLogs(models.Model):
    id = models.IntegerField(verbose_name = 'id', primary_key = True)
    user_id = models.ForeignKey(Users, verbose_name = 'user_ID', blank = True, null = True, on_delete = models.SET_NULL)
    session_id = models.CharField(verbose_name = 'session_id', max_length = 255)
    http_method = models.CharField(verbose_name = 'http_method', max_length = 20)
    url = models.CharField(verbose_name = 'url', max_length = 255)
    user_action = models.CharField(verbose_name = 'user_action', max_length = 30)
    created_at = models.DateTimeField(verbose_name = 'created_at')

    class Meta(object):
        verbose_name_plural = 'Request Logs'
