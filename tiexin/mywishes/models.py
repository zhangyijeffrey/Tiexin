from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wish(models.Model):
	# django default primary key
	# id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	proposed_by = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField()
	location = models.CharField(max_length=200)
	publish_time = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	content = models.TextField()
	status = models.CharField(max_length=20)

class WishComment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	wish = models.ForeignKey(Wish, on_delete=models.CASCADE)
	content = models.CharField(max_length=1000)
	publish_time = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

class WishPopularity(models.Model):
	wish = models.ForeignKey(Wish, on_delete=models.CASCADE)
	n_likes = models.PositiveIntegerField()
	n_dislikes = models.PositiveIntegerField()
	n_views = models.PositiveIntegerField()
	n_forwards = models.PositiveIntegerField()
	n_comments = models.PositiveIntegerField()
	last_modified = models.DateTimeField(auto_now=True)

class WishMedia(models.Model):
	wish = models.ForeignKey(Wish, on_delete=models.CASCADE)
	upload_user = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)
	description = models.CharField(max_length=200)
	media_file = models.FileField(upload_to='%Y/%m/%d/')
