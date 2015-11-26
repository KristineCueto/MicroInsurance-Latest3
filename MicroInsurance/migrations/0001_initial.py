# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('branchName', models.CharField(max_length=100, default='')),
                ('branchAddress', models.TextField(max_length=200, default='')),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
    ]
