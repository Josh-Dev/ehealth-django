# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehealth_project', '0010_auto_20160318_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='slug',
            field=models.SlugField(default=2),
            preserve_default=False,
        ),
    ]
