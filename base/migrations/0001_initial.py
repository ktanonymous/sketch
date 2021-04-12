# Generated by Django 3.1 on 2021-04-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLogs',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('user_id', models.IntegerField(verbose_name='user_ID')),
                ('session_id', models.CharField(max_length=255, verbose_name='session_id')),
                ('http_method', models.CharField(max_length=20, verbose_name='http_method')),
                ('url', models.CharField(max_length=255, verbose_name='url')),
                ('user_action', models.CharField(max_length=30, verbose_name='user_action')),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='ResponseLogs',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('user_id', models.IntegerField(verbose_name='user_ID')),
                ('session_id', models.CharField(max_length=255, verbose_name='session_id')),
                ('http_method', models.CharField(max_length=20, verbose_name='http_method')),
                ('url', models.CharField(max_length=255, verbose_name='url')),
                ('status_code', models.IntegerField(verbose_name='calendar_path')),
                ('text_phrase', models.CharField(max_length=255, verbose_name='text_phrase')),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ユーザーID')),
                ('first_name', models.CharField(max_length=30, verbose_name='名前')),
                ('first_name_pronunciation', models.CharField(max_length=30, null=True, verbose_name='なまえ')),
                ('last_name', models.CharField(max_length=30, verbose_name='名字')),
                ('last_name_pronunciation', models.CharField(max_length=30, null=True, verbose_name='みょうじ')),
                ('nickname', models.CharField(max_length=10, null=True, verbose_name='表示名')),
                ('age', models.IntegerField(null=True, verbose_name='年齢')),
                ('sex', models.BinaryField(null=True, verbose_name='性別')),
                ('mail_address', models.CharField(max_length=255, verbose_name='メールアドレス')),
                ('password', models.CharField(max_length=255, verbose_name='パスワード')),
                ('icon_path', models.CharField(max_length=255, null=True, verbose_name='icon_path')),
                ('calendar_path', models.CharField(max_length=255, null=True, verbose_name='calendar_path')),
                ('created_at', models.DateTimeField(verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(verbose_name='更新日時')),
            ],
        ),
    ]
