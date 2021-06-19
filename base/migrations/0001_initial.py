# Generated by Django 3.1 on 2021-06-19 02:41

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
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='AdjustingSchedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=30, verbose_name='イベント名')),
                ('date1_start', models.DateTimeField(blank=True, null=True, verbose_name='date1_start')),
                ('date1_end', models.DateTimeField(blank=True, null=True, verbose_name='date1_end')),
                ('date2_start', models.DateTimeField(blank=True, null=True, verbose_name='date2_start')),
                ('date2_end', models.DateTimeField(blank=True, null=True, verbose_name='date2_end')),
                ('date3_start', models.DateTimeField(blank=True, null=True, verbose_name='date3_start')),
                ('date3_end', models.DateTimeField(blank=True, null=True, verbose_name='date3_end')),
                ('date4_start', models.DateTimeField(blank=True, null=True, verbose_name='date4_start')),
                ('date4_end', models.DateTimeField(blank=True, null=True, verbose_name='date4_end')),
                ('date5_start', models.DateTimeField(blank=True, null=True, verbose_name='date5_start')),
                ('date5_end', models.DateTimeField(blank=True, null=True, verbose_name='date5_end')),
                ('current_user_num', models.IntegerField(blank=True, verbose_name='current_user_num')),
                ('friend1', models.ForeignKey(db_column='friend1_id', on_delete=django.db.models.deletion.CASCADE, related_name='friend1', to=settings.AUTH_USER_MODEL, verbose_name='友達1')),
                ('friend2', models.ForeignKey(blank=True, db_column='friend2_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friend2', to=settings.AUTH_USER_MODEL, verbose_name='友達2')),
                ('friend3', models.ForeignKey(blank=True, db_column='friend3_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friend3', to=settings.AUTH_USER_MODEL, verbose_name='友達3')),
                ('proposer', models.ForeignKey(db_column='proposer_id', on_delete=django.db.models.deletion.CASCADE, related_name='proposer', to=settings.AUTH_USER_MODEL, verbose_name='proposer')),
            ],
            options={
                'verbose_name_plural': 'AdjustingSchedules',
                'db_table': 'adjusting_schedules',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=30, verbose_name='イベント名')),
                ('date_start', models.DateTimeField(verbose_name='開始日時')),
                ('date_end', models.DateTimeField(verbose_name='終了日時')),
                ('participant', models.ForeignKey(db_column='participant_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='participant_id')),
            ],
            options={
                'verbose_name_plural': 'Events',
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('event_name', models.CharField(max_length=255, verbose_name='イベント名')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('adjusting_schedule', models.ForeignKey(blank=True, db_column='adjusting_schedule_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='base.adjustingschedule', verbose_name='adjusting_schedule_id')),
                ('event', models.ForeignKey(blank=True, db_column='event_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='base.event', verbose_name='event_id')),
                ('receiver', models.ForeignKey(db_column='receiver_id', on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL, verbose_name='receiver_id')),
                ('sender', models.ForeignKey(db_column='sender_id', on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL, verbose_name='sender_id')),
            ],
            options={
                'verbose_name_plural': 'Informations',
                'db_table': 'informations',
            },
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('follow_user', models.ForeignKey(db_column='follow_user_id', on_delete=django.db.models.deletion.CASCADE, related_name='follow_user', to=settings.AUTH_USER_MODEL, verbose_name='follow_user')),
                ('followed_user', models.ForeignKey(db_column='followed_user_id', on_delete=django.db.models.deletion.CASCADE, related_name='followed_user', to=settings.AUTH_USER_MODEL, verbose_name='followed_user')),
            ],
            options={
                'verbose_name_plural': 'Friends',
                'db_table': 'friends',
            },
        ),
    ]
