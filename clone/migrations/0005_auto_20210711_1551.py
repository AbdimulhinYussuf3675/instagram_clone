# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-07-11 12:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clone', '0004_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='followed',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='follower',
        ),
        migrations.AddField(
            model_name='follow',
            name='user_from',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='rel_from_set', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='follow',
            name='user_to',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='rel_to_set', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='commenting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
