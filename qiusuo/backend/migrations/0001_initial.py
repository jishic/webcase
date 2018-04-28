# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attention',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(verbose_name='用户名', max_length=20)),
                ('teachername', models.CharField(verbose_name='用户名', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Forbid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('teachername', models.CharField(verbose_name='用户名', max_length=20)),
                ('banedname', models.CharField(verbose_name='被禁名', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('roomnum', models.CharField(verbose_name='直播间号', max_length=6, default='')),
                ('roomtitle', models.CharField(verbose_name='直播间标题', max_length=40, blank=True, null=True, default='')),
                ('isstream', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(verbose_name='用户名', primary_key=True, max_length=20, serialize=False)),
                ('password', models.CharField(verbose_name='用户密码', max_length=42)),
                ('telephone', models.CharField(verbose_name='用户电话', max_length=11)),
                ('email', models.CharField(verbose_name='用户邮箱', max_length=20, blank=True, null=True, default='')),
                ('isTea', models.BooleanField(default=False)),
                ('gender', models.BooleanField(default=False)),
                ('imgpath', models.CharField(verbose_name='图片路径', max_length=160, default='')),
            ],
        ),
        migrations.AddField(
            model_name='studio',
            name='teachername',
            field=models.ForeignKey(to='backend.User'),
        ),
        migrations.AlterUniqueTogether(
            name='forbid',
            unique_together=set([('teachername', 'banedname')]),
        ),
        migrations.AlterUniqueTogether(
            name='attention',
            unique_together=set([('username', 'teachername')]),
        ),
    ]
