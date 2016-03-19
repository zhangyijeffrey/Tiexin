# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-04 05:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0008_auto_20160225_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='toysource',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='toysource',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='toysource',
            name='is_final_quote_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='toysource',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]