# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-03 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
        ('ventas', '0003_auto_20161128_0327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='id_venta',
            new_name='id_servicio',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='producto',
        ),
        migrations.AddField(
            model_name='venta',
            name='servicio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.Servicio'),
            preserve_default=False,
        ),
    ]
