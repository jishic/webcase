# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studio',
            name='stuimgpath',
            field=models.CharField(verbose_name='直播间图片路径', max_length=160, default=''),
        ),
    ]
