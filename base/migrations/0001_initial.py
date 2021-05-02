# Generated by Django 3.1 on 2021-05-02 02:53

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=10, validators=[django.contrib.auth.validators.UnicodeUsernameValidator], verbose_name='ユーザー名')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='メールアドレス')),
                ('password', models.CharField(max_length=255, verbose_name='パスワード')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=30, verbose_name='イベント名')),
                ('date_start', models.DateTimeField(verbose_name='開始日時')),
                ('date_end', models.DateTimeField(verbose_name='終了日時')),
                ('user_id', models.IntegerField(verbose_name='user_id')),
            ],
            options={
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('follow_user_id', models.ForeignKey(blank=True, db_column='follow_user_id', on_delete=django.db.models.deletion.CASCADE, related_name='follow_userid', to=settings.AUTH_USER_MODEL, verbose_name='follow_user_id')),
                ('followed_user_id', models.ForeignKey(blank=True, db_column='followed_user_id', on_delete=django.db.models.deletion.CASCADE, related_name='followed_userid', to=settings.AUTH_USER_MODEL, verbose_name='followed_user_id')),
            ],
            options={
                'verbose_name_plural': 'Friends',
            },
        ),
    ]
