# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDataUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField(max_length=400)),
                ('upload_date', models.DateTimeField(verbose_name=b'date uploaded')),
                ('filescount', models.IntegerField(default=0)),
            ],
        ),
    ]
