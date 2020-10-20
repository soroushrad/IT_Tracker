# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-08 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assets', '0010_auto_20201008_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner_asset_3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Asset3', to='Assets.Laptops', verbose_name='Asset 3'),
        ),
    ]