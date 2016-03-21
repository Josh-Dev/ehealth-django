# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehealth_project', '0005_auto_20160310_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
