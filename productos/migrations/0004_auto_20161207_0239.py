# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-07 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_salida_id_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stock_producto',
            field=models.PositiveIntegerField(default=0),
        ),
    ]