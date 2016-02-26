# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-23 21:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import toys.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('toys', '0004_auto_20160216_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToySource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=100)),
                ('original_cost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('original_vendor', models.CharField(max_length=100)),
                ('has_original_receipt', models.CharField(max_length=10)),
                ('purchase_time', models.PositiveSmallIntegerField()),
                ('exterior', models.CharField(max_length=100)),
                ('functionality', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
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
                ('uuid', models.CharField(default=toys.models.get_uuid, editable=False, max_length=36)),
                ('num_images', models.PositiveSmallIntegerField(default=0)),
                ('submit_date', models.DateTimeField()),
                ('instant_quote_point', models.PositiveIntegerField(default=0)),
                ('instant_quote_discount', models.PositiveIntegerField(default=0)),
                ('is_instant_quote_accepted', models.CharField(max_length=10, null=True)),
                ('status', models.CharField(max_length=100)),
                ('status_last_modified', models.DateTimeField(null=True)),
                ('receive_date', models.DateTimeField(null=True)),
                ('final_quote', models.PositiveIntegerField(default=0)),
                ('is_final_quote_accepted', models.CharField(max_length=10, null=True)),
                ('is_complete', models.CharField(default='no', max_length=10)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
