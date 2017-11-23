# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 15:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forestry_game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('mapdata', models.TextField(default='')),
                ('mapinfo', models.TextField(default='')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('distance', models.IntegerField(default=0)),
                ('gas_consumption', models.IntegerField(default=0)),
                ('duration', models.IntegerField(default=0)),
                ('logs', models.TextField(default='')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forestry_game.Level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='execution',
            name='map',
        ),
        migrations.RemoveField(
            model_name='execution',
            name='user',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Execution',
        ),
        migrations.DeleteModel(
            name='Map',
        ),
    ]
