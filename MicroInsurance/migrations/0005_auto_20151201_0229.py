# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('MicroInsurance', '0004_promo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promo',
            old_name='promoDateCreated',
            new_name='PromoDateCreated',
        ),
        migrations.AlterField(
            model_name='promo',
            name='PromoLess',
            field=models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Promo Less', default=1.0, decimal_places=2, max_digits=18),
        ),
    ]
