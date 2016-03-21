# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehealth_project', '0003_remove_folder_parent_folder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='last_access',
        ),
    ]
