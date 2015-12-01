# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('MicroInsurance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='SKU_AgeFrom',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(18)], verbose_name='Insurance Age From', default=18),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='SKU_AgeTo',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(19)], verbose_name='Insurance Age To', default=19),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='SKU_BasedPrice',
            field=models.DecimalField(default=0.0, decimal_places=2, max_digits=18, verbose_name='Insurance Based Price'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='SKU_EffectDate',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Insurance Effectivity Date'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='SKU_LimitPerPerson',
            field=models.IntegerField(default=1, verbose_name='Insurance Limit Per Person'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='SKU_Name',
            field=models.CharField(default='', max_length=100, verbose_name='Insurance Name'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='SKU_SellingPrice',
            field=models.DecimalField(default=0.0, decimal_places=2, max_digits=18, verbose_name='Insurance Selling Price'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='SKU_ValidityDays',
            field=models.IntegerField(default=0, verbose_name='Insurance Validity Days'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='SKU_underWriter',
            field=models.ForeignKey(to='MicroInsurance.UnderWriter', default='', verbose_name='Under Writer Name'),
        ),
    ]
