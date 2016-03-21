# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('privacy', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('source', models.CharField(max_length=128)),
                ('summary', models.TextField()),
                ('readability_score', models.IntegerField(default=0)),
                ('objectivity_score', models.IntegerField(default=0)),
                ('sentimentality_score', models.IntegerField(default=0)),
                ('folder', models.ForeignKey(to='ehealth_project.Folder')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dob', models.DateField()),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(max_length=128, blank=True)),
                ('city', models.CharField(default=b'', max_length=64)),
                ('post_code', models.CharField(max_length=8)),
                ('gender', models.CharField(max_length=128)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='folder',
            name='user',
            field=models.ForeignKey(to='ehealth_project.UserProfile'),
            preserve_default=True,
        ),
    ]
