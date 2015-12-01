# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('branchName', models.CharField(verbose_name='Branch Name', default='', max_length=100)),
                ('branchAddress', models.TextField(verbose_name='Branch Address', default='', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('SKU_Name', models.CharField(default='', max_length=100)),
                ('SKU_BasedPrice', models.DecimalField(default=0.0, max_digits=18, decimal_places=2)),
                ('SKU_SellingPrice', models.DecimalField(default=0.0, max_digits=18, decimal_places=2)),
                ('SKU_ValidityDays', models.IntegerField(default=0)),
                ('SKU_EffectDate', models.DateTimeField(default=datetime.datetime.now)),
                ('SKU_AgeFrom', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(18)], default=18)),
                ('SKU_AgeTo', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(19)], default=19)),
                ('SKU_LimitPerPerson', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UnderWriter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('underWriterName', models.CharField(verbose_name='Under Writer Name', default='', max_length=100)),
                ('underWriterAddress', models.TextField(verbose_name='Under Writer Address', default='', max_length=200)),
                ('underWriterContact', models.CharField(verbose_name='Under Writer Contact No', default='', max_length=13)),
            ],
        ),
        migrations.AddField(
            model_name='insurance',
            name='SKU_underWriter',
            field=models.ForeignKey(to='MicroInsurance.UnderWriter', default=''),
        ),
    ]
