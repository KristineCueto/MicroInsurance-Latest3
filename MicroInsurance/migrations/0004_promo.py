# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('MicroInsurance', '0003_auto_20151201_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PromoName', models.CharField(default='', verbose_name='Promo Name', max_length=50)),
                ('PromoDateStart', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date Start')),
                ('PromoDateEnd', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date End')),
                ('PromoNoOfSku', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], default=1, verbose_name='Number of SKU to be promo')),
                ('PromoLess', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], default=1, verbose_name='Promo Less')),
                ('promoDateCreated', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date Created')),
                ('PromoStatus', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='A', verbose_name='Status', max_length=1)),
                ('Promo_SKU', models.ForeignKey(default='', verbose_name='Insurance Name', to='MicroInsurance.Insurance')),
            ],
        ),
    ]
