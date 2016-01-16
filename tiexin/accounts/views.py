from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, RedirectView
from weixin.client import WeixinAPI
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, AnonymouseUser
from .models import WeixinAuth, WeixinProfile


# Create your views here.
class Login(TemplateView):
	template_name = 'accounts/login.html'

class LoginWeixin(RedirectView):

	def get_redirect_url(self, *args, **kwargs):
		user = self.request.user

		if user.is_authenticated():
			url = reverse('accounts:login-success')
		else:
			redirect_uri = settings.WEB_URL + reverse('accounts:login-weixin-get-code')
			print redirect_uri
			scope = ('snsapi_login',)
			api = WeixinAPI(appid=settings.APP_ID, app_secret=settings.APP_SECRET, redirect_uri=redirect_uri)
			url = api.get_authorize_url(scope=scope)

		return url

class WeixinAuth(RedirectView):
	def get_redirect_url(self, *arg, **kwargs):
		code = self.request.GET.get('code','')
		if code == '':
			url = settings.WEB_URL
		else:
			api = WeixinAPI(appid=settings.APP_ID, app_secret=settings.APP_SECRET)
			# exchange code for access token and related auth info
			auth_info = api.exchange_code_for_access_token(code=code)
			# get user profile from Weixin
			api = WeixinAPI(access_toke=auth_info['access_token'])
			user_profile = api.user(openid=auth_info['openid'])

			# create user using openid only and add it to django's User model
			# password is not set (set_unusable_password() when it's not provided)
			# add auth_info and user_profile to WeixinAuth and WeixinProfile models
			# auth_info keys: access_token, expire_in, refresh_token, openid, scope
			# user_profile keys: openid, nickname, sex, province, city, country, headimgurl, privilege, unionid

			auth_user = User.objects.create_user(username=auth_info['openid'])
			auth_user.save()


		return url

class LoginSuccess(TemplateView):
	template_name = 'accounts/login_success.html'

class Logout(RedirectView):

	def get_redirect_url(self, *args, **kwargs):
		url = reverse('accounts:login')
		logout(self.request)
		return url