# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehealth_project', '0008_userprofile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pic',
            field=models.ImageField(default=b'/static/images/blank.jpg', upload_to=b'', blank=True),
        ),
    ]
