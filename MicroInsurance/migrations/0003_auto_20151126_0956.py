# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MicroInsurance', '0002_auto_20151126_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='underwriter',
            name='underWriterContact',
            field=models.CharField(max_length=13, verbose_name='Under Writer Contact No', default=''),
        ),
        migrations.AlterField(
            model_name='underwriter',
            name='underWriterAddress',
            field=models.TextField(max_length=200, verbose_name='Under Writer Address', default=''),
        ),
        migrations.AlterField(
            model_name='underwriter',
            name='underWriterName',
            field=models.CharField(max_length=100, verbose_name='Under Writer Name', default=''),
        ),
    ]
