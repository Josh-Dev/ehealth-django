# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehealth_project', '0011_folder_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='objectivity_score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='page',
            name='readability_score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='page',
            name='sentimentality_score',
            field=models.FloatField(default=0),
        ),
    ]
