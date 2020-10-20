# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-08 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptops',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Laptop ID')),
                ('model', models.TextField(max_length=150, verbose_name='Model')),
                ('ram', models.IntegerField(null=True, verbose_name='RAM')),
                ('HDD_status', models.IntegerField(choices=[(1, 'SSD 512'), (2, 'SSD_256'), (3, 'HDD_1T'), (4, 'HDD_512')], verbose_name='Hard Model')),
                ('Win_status', models.IntegerField(choices=[(1, 'Windows 7 32 bit'), (2, 'Windows 7 64 bit'), (3, 'Windows 8 '), (4, 'Windows_10')], verbose_name='Windows Status')),
                ('Laptop_status', models.IntegerField(choices=[(1, '\u0644\u067e \u062a\u0627\u067e \u062f\u0631 \u0627\u0646\u0628\u0627\u0631 \u0627\u0633\u062a'), (2, '\u0644\u067e \u062a\u0627\u067e \u062f\u0631 \u062f\u0633\u062a \u06a9\u0627\u0631\u0628\u0631 \u0627\u0633\u062a'), (3, '\u0644\u067e \u062a\u0627\u067e \u062f\u0631 \u062d\u0627\u0644 \u062a\u0639\u0645\u06cc\u0631 \u0627\u0633\u062a'), (4, '\u0644\u067e \u062a\u0627\u067e \u0627\u0633\u0642\u0627\u0637 \u0634\u062f\u0647 \u0627\u0633\u062a')], verbose_name='Laptop Status')),
            ],
        ),
    ]
