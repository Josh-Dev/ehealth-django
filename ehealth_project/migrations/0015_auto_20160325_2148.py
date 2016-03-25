# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehealth_project', '0014_remove_userprofile_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address_1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='post_code',
        ),
    ]
