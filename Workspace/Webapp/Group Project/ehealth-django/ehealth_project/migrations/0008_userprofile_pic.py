# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehealth_project', '0007_userprofile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pic',
            field=models.ImageField(default=b'/static/image.jpg', upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
