# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-04 05:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import toys.models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0009_auto_20160303_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToyInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=100)),
                ('original_vendor', models.CharField(max_length=100, null=True)),
                ('purchase_time', models.CharField(max_length=50)),
                ('exterior', models.CharField(max_length=100)),
                ('functionality', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('buy_in_price_point', models.PositiveIntegerField(default=0)),
                ('sell_price_point', models.PositiveIntegerField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=100)),
                ('status_last_modified', models.DateTimeField(null=True)),
                ('num_images', models.PositiveSmallIntegerField(default=0)),
                ('image1', models.ImageField(max_length=200, null=True, upload_to=toys.models.get_fullsize_image_path)),
                ('image2', models.ImageField(max_length=200, null=True, upload_to=toys.models.get_fullsize_image_path)),
                ('image3', models.ImageField(max_length=200, null=True, upload_to=toys.models.get_fullsize_image_path)),
                ('image4', models.ImageField(max_length=200, null=True, upload_to=toys.models.get_fullsize_image_path)),
                ('image5', models.ImageField(max_length=200, null=True, upload_to=toys.models.get_fullsize_image_path)),
                ('image1_thumbnail', models.ImageField(max_length=200, null=True, upload_to=toys.models.get_thumbnail_image_path)),
                ('image2_thumbnail', models.ImageField(max_length=200, null=True, upload_to=toys.models.get_thumbnail_image_path)),
                ('image3_thumbnail', models.ImageField(max_length=200, null=True, upload_to=toys.models.get_thumbnail_image_path)),
                ('image4_thumbnail', models.ImageField(max_length=200, null=True, upload_to=toys.models.get_thumbnail_image_path)),
                ('image5_thumbnail', models.ImageField(max_length=200, null=True, upload_to=toys.models.get_thumbnail_image_path)),
                ('toy_source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='toys.ToySource')),
            ],
        ),
    ]
