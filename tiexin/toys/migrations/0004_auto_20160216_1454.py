# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 22:54
from __future__ import unicode_literals

from django.db import migrations, models
import toys.models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0003_auto_20160216_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='image1_thumbnail',
            field=models.ImageField(max_length=200, null=True, upload_to=toys.models.get_thumbnail_image_path),
        ),
        migrations.AlterField(
            model_name='toy',
            name='image2',
            field=models.ImageField(max_length=200, null=True, upload_to=toys.models.get_fullsize_image_path),
        ),
        migrations.AlterField(
            model_name='toy',
            name='image2_thumbnail',
            field=models.ImageField(max_length=200, null=True, upload_to=toys.models.get_thumbnail_image_path),
        ),
        migrations.AlterField(
            model_name='toy',
            name='image3',
            field=models.ImageField(max_length=200, null=True, upload_to=toys.models.get_fullsize_image_path),
        ),
        migrations.AlterField(
            model_name='toy',
            name='image3_thumbnail',
            field=models.ImageField(max_length=200, null=True, upload_to=toys.models.get_thumbnail_image_path),
        ),
        migrations.AlterField(
            model_name='toy',
            name='image4',
            field=models.ImageField(max_length=200, null=True, upload_to=toys.models.get_fullsize_image_path),
        ),
        migrations.AlterField(
            model_name='toy',
            name='image4_thumbnail',
            field=models.ImageField(max_length=200, null=True, upload_to=toys.models.get_thumbnail_image_path),
        ),
        migrations.AlterField(
            model_name='toy',
            name='image5',
            field=models.ImageField(max_length=200, null=True, upload_to=toys.models.get_fullsize_image_path),
        ),
        migrations.AlterField(
            model_name='toy',
            name='image5_thumbnail',
            field=models.ImageField(max_length=200, null=True, upload_to=toys.models.get_thumbnail_image_path),
        ),
    ]
