# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('MicroInsurance', '0002_auto_20151127_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='branchDateCreated',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date Created'),
        ),
        migrations.AddField(
            model_name='branch',
            name='branchStatus',
            field=models.CharField(default='A', max_length=1, choices=[('A', 'Active'), ('I', 'Inactive')], verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='SKU_DateCreated',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date Created'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='SKU_Status',
            field=models.CharField(default='A', max_length=1, choices=[('A', 'Active'), ('I', 'Inactive')], verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='underwriter',
            name='underWriterDateCreated',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date Created'),
        ),
        migrations.AddField(
            model_name='underwriter',
            name='underWriterStatus',
            field=models.CharField(default='A', max_length=1, choices=[('A', 'Active'), ('I', 'Inactive')], verbose_name='Status'),
        ),
    ]
