# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-08 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assets', '0008_auto_20201008_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_asset_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Asset1', to='Assets.Laptops', verbose_name='Asset 1'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_asset_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Asset2', to='Assets.Laptops', verbose_name='Asset 2'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_asset_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Asset3', to='Assets.Laptops', verbose_name='Asset 3'),
        ),
    ]
