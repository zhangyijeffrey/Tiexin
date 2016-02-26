# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 22:31
from __future__ import unicode_literals

from django.db import migrations, models
import toys.models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0002_auto_20160216_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='image1',
            field=models.ImageField(max_length=200, null=True, upload_to=toys.models.get_fullsize_image_path),
        ),
    ]