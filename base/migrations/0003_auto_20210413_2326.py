# Generated by Django 3.1 on 2021-04-13 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210413_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestlogs',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.users', verbose_name='user_ID'),
        ),
        migrations.AlterField(
            model_name='responselogs',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.users', verbose_name='user_ID'),
        ),
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='年齢'),
        ),
        migrations.AlterField(
            model_name='users',
            name='calendar_path',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='calendar_path'),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name_pronunciation',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='なまえ'),
        ),
        migrations.AlterField(
            model_name='users',
            name='icon_path',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='icon_path'),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name_pronunciation',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='みょうじ'),
        ),
        migrations.AlterField(
            model_name='users',
            name='nickname',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='表示名'),
        ),
        migrations.AlterField(
            model_name='users',
            name='sex',
            field=models.BinaryField(blank=True, null=True, verbose_name='性別'),
        ),
    ]
