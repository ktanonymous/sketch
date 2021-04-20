# Generated by Django 3.1 on 2021-04-18 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated_at')),
                ('follow_user_id', models.ForeignKey(blank=True, db_column='follow_user_id', on_delete=django.db.models.deletion.CASCADE, related_name='follow_userid', to=settings.AUTH_USER_MODEL, verbose_name='follow_user_id')),
                ('followed_user_id', models.ForeignKey(blank=True, db_column='followed_user_id', on_delete=django.db.models.deletion.CASCADE, related_name='followed_userid', to=settings.AUTH_USER_MODEL, verbose_name='followed_user_id')),
            ],
            options={
                'verbose_name_plural': 'Friends',
            },
        ),
    ]
