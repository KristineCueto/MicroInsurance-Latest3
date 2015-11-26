# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MicroInsurance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnderWriter',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('underWriterName', models.CharField(max_length=100, default='')),
                ('underWriterAddress', models.TextField(max_length=200, default='')),
            ],
        ),
        migrations.AlterField(
            model_name='branch',
            name='branchAddress',
            field=models.TextField(max_length=200, verbose_name='Branch Address', default=''),
        ),
        migrations.AlterField(
            model_name='branch',
            name='branchName',
            field=models.CharField(max_length=100, verbose_name='Branch Name', default=''),
        ),
    ]
