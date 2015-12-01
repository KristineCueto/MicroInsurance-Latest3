# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('MicroInsurance', '0005_auto_20151201_0229'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('userTypeName', models.CharField(max_length=50, verbose_name='UserType Name', default='')),
                ('userTypeDateCreated', models.DateTimeField(verbose_name='Date Created', default=datetime.datetime.now)),
                ('userTypeStatus', models.CharField(verbose_name='Status', max_length=1, choices=[('A', 'Active'), ('I', 'Inactive')], default='A')),
            ],
        ),
    ]
