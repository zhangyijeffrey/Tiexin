 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid;

# Create your models here.

def get_fullsize_image_path(instance, filename):
	if isinstance(instance, ToySource):
		folder_name = 'source'
	elif isinstance(instance, ToyInventory):
		folder_name = 'inventory'
	else:
		folder_name = 'unknown'
	return '/'.join(['toys', folder_name, instance.uuid, 'fullsize', filename])

def get_thumbnail_image_path(instance, filename):
	if isinstance(instance, ToySource):
		folder_name = 'source'
	elif isinstance(instance, ToyInventory):
		folder_name = 'inventory'	
	else:
		folder_name = 'unknown'
	return '/'.join(['toys', folder_name, instance.uuid, 'thumbnail', filename])

def get_uuid():
	return str(uuid.uuid4())

class Toy(models.Model):
	# django default primary key
	# id = models.AutoField(primary_key=True)
	# uuid is used for user upload picture folder name
	uuid = models.CharField(max_length=36, default=get_uuid, editable=False)
	title = models.CharField(max_length=200)
	status = models.CharField(max_length=100)
	description = models.TextField()
	brand = models.CharField(max_length=100)


	sold_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sold_by')
	sold_by_propose_price = models.DecimalField(max_digits=6, decimal_places=2,default=0)
	sold_by_propose_time = models.DateTimeField()
	sold_by_accept_price = models.DecimalField(max_digits=6, decimal_places=2,default=0)
	sold_by_accept_time = models.DateTimeField(null=True)

	sell_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	sold_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sold_to', null=True)
	sold_to_time = models.DateTimeField(null=True)

	publish_time = models.DateTimeField(null=True)
	last_modified = models.DateTimeField(auto_now=True)

	num_images = models.PositiveSmallIntegerField(default=0)
	image1 = models.ImageField(upload_to=get_fullsize_image_path, max_length=200, null=True)
	image2 = models.ImageField(upload_to=get_fullsize_image_path, max_length=200, null=True)
 	image3 = models.ImageField(upload_to=get_fullsize_image_path, max_length=200, null=True)
 	image4 = models.ImageField(upload_to=get_fullsize_image_path, max_length=200, null=True)
 	image5 = models.ImageField(upload_to=get_fullsize_image_path, max_length=200, null=True)
	image1_thumbnail = models.ImageField(upload_to=get_thumbnail_image_path, max_length=200, null=True)
	image2_thumbnail = models.ImageField(upload_to=get_thumbnail_image_path, max_length=200, null=True)
 	image3_thumbnail = models.ImageField(upload_to=get_thumbnail_image_path, max_length=200, null=True)
 	image4_thumbnail = models.ImageField(upload_to=get_thumbnail_image_path, max_length=200, null=True)
 	# image5_thumbnail = models.ImageField(upload_to=get_thumbnail_image_path, max_length=200, null=True)



class ToySource(models.Model):

	class Meta:
		permissions = (
			('approve_toy', "Can approve a user's toy and finalize the quote"),
		)


	# django default primary key
	# id = models.AutoField(primary_key=True)

	# User entry
	title = models.CharField(max_length=200)
	brand = models.CharField(max_length=100)
	original_cost = models.PositiveIntegerField(null=True, blank=True)
	original_vendor = models.CharField(max_length=100)
	has_original_receipt = models.CharField(max_length=10)
	purchase_time = models.CharField(max_length=50)
	exterior = models.CharField(max_length=100)
	functionality = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	image1 = models.ImageField(upload_to=get_fullsize_image_path, max_length=200, null=True)
	image2 = models.ImageField(upload_to=get_fullsize_image_path, max_length=200, null=True)
 	image3 = models.ImageField(upload_to=get_fullsize_image_path, max_length=200, null=True)
 	image4 = models.ImageField(upload_to=get_fullsize_image_path, max_length=200, null=True)
 	image5 = models.ImageField(upload_to=get_fullsize_image_path, max_length=200, null=True)
	image1_thumbnail = models.ImageField(upload_to=get_thumbnail_image_path, max_length=200, null=True)
	image2_thumbnail = models.ImageField(upload_to=get_thumbnail_image_path, max_length=200, null=True)
 	image3_thumbnail = models.ImageField(upload_to=get_thumbnail_image_path, max_length=200, null=True)
 	image4_thumbnail = models.ImageField(upload_to=get_thumbnail_image_path, max_length=200, null=True)
 	image5_thumbnail = models.ImageField(upload_to=get_thumbnail_image_path, max_length=200, null=True)

 	# More Toy/User info
	# uuid is used for user upload picture folder name
	uuid = models.CharField(max_length=36, default=get_uuid, editable=False)
	seller = models.ForeignKey(User, on_delete=models.PROTECT)
	num_images = models.PositiveSmallIntegerField(default=0)
	submit_date = models.DateTimeField()
	instant_quote_point = models.PositiveIntegerField(default=0)
	instant_quote_discount = models.PositiveIntegerField(default=0)
	is_instant_quote_accepted = models.NullBooleanField()
	status = models.CharField(max_length=100)
	status_last_modified = models.DateTimeField(null=True)

	# Admin entry
	receive_date = models.DateTimeField(null=True)
	final_quote = models.PositiveIntegerField(default=0)
	comment = models.TextField(null=True, blank=True)
	is_final_quote_accepted = models.BooleanField(default=False)
	is_complete = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title + '-' + self.brand + '-' + self.original_vendor

class ToyInventory(models.Model):
	toy_source = models.ForeignKey(ToySource, on_delete=models.PROTECT)
	title = models.CharField(max_length=200)
	brand = models.CharField(max_length=100)
	original_vendor = models.CharField(max_length=100, null=True)
	purchase_time = models.CharField(max_length=50)
	exterior = models.CharField(max_length=100)
	functionality = models.CharField(max_length=100)
	description = models.TextField()

	buy_in_price_point = models.PositiveIntegerField(default=0)
	sell_price_point = models.PositiveIntegerField()

	add_time = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=100)
	status_last_modified = models.DateTimeField(null=True)

	num_images = models.PositiveSmallIntegerField(default=0)
	image1 = models.ImageField(upload_to=get_fullsize_image_path, max_length=200, null=True)
	image2 = models.ImageField(upload_to=get_fullsize_image_path, max_length=200, null=True)
 	image3 = models.ImageField(upload_to=get_fullsize_image_path, max_length=200, null=True)
 	image4 = models.ImageField(upload_to=get_fullsize_image_path, max_length=200, null=True)
 	image5 = models.ImageField(upload_to=get_fullsize_image_path, max_length=200, null=True)
	image1_thumbnail = models.ImageField(upload_to=get_thumbnail_image_path, max_length=200, null=True)
	image2_thumbnail = models.ImageField(upload_to=get_thumbnail_image_path, max_length=200, null=True)
 	image3_thumbnail = models.ImageField(upload_to=get_thumbnail_image_path, max_length=200, null=True)
 	image4_thumbnail = models.ImageField(upload_to=get_thumbnail_image_path, max_length=200, null=True)
 	image5_thumbnail = models.ImageField(upload_to=get_thumbnail_image_path, max_length=200, null=True)