 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.


# User model fields:
# -id
# -password  -- for Weixin users, this will be set as 'WeixinPwd'
# -last_login
# -is_superuser
# -username -- store Weixin openid, the current length of username is 30 and openid is 28
# 		   -- it is possible to change the username length in database
# -first_name
# -last_name
# -email
# -is_staff
# -is_active
# -date_joined

class WeixinAuth(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	openid = models.CharField(max_length=100)
	access_token = models.CharField(max_length=1024)
	expires_in = models.PositiveIntegerField()
	refresh_token = models.CharField(max_length=1024)
	scope = models.CharField(max_length=400)
	last_modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.user.weixinprofile.nickname

class WeixinProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	openid = models.CharField(max_length=100)
	nickname = models.CharField(max_length=100)
	sex = models.PositiveSmallIntegerField(choices=((1, 'M'),(2, 'F'), (0, 'X')))
	province = models.CharField(max_length=20)
	city = models.CharField(max_length=20)
	country = models.CharField(max_length=20)
	headimgurl = models.URLField(max_length=300)
	privilege = models.CharField(max_length=100)
	unionid = models.CharField(max_length=100)
	last_modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.nickname

class TiexinProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	cell = models.CharField(max_length=20, blank=True)
	qq = models.CharField(max_length=20, blank=True)
	age = models.PositiveSmallIntegerField(null=True, blank=True)
	last_modified = models.DateTimeField(auto_now=True)
	is_staff = models.BooleanField(default=False)

	def __unicode__(self):
		return self.user.weixinprofile.nickname

