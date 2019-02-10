# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-23 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190122_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='spell',
            name='element',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='spell',
            name='spell_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spell',
            name='star_rank',
            field=models.IntegerField(null=True),
        ),
    ]