# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehealth_project', '0004_remove_page_last_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='source',
            field=models.CharField(max_length=128),
        ),
    ]
