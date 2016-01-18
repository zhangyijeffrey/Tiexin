from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, RedirectView
from weixin.client import WeixinAPI
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import WeixinAuth, WeixinProfile


# Create your views here.
class Login(TemplateView):
	template_name = 'accounts/login.html'

class LoginWeixin(RedirectView):

	def get_redirect_url(self, *args, **kwargs):
		url = reverse('accounts:auth-weixin')

		# user = self.request.user
		# if user.is_authenticated():
		# 	url = reverse('accounts:login-success')
		# else:
		# 	redirect_uri = settings.WEB_URL + reverse('accounts:weixin-auth')
		# 	print redirect_uri
		# 	scope = ('snsapi_login',)
		# 	api = WeixinAPI(appid=settings.APP_ID, app_secret=settings.APP_SECRET, redirect_uri=redirect_uri)
		# 	url = api.get_authorize_url(scope=scope)

		return url

class AuthWeixin(RedirectView):
	def get_redirect_url(self, *arg, **kwargs):
		# code = self.request.GET.get('code','')
		code = settings.TEST_CODE
		if code == '':
			# redirect to warning page, and then log in as anonymous user
			url = settings.WEB_URL
		else:
			# api = WeixinAPI(appid=settings.APP_ID, app_secret=settings.APP_SECRET)
			# exchange code for access token and related auth info
			# auth_info = api.exchange_code_for_access_token(code=code)
			auth_info = settings.TEST_AUTH_INFO

			# check if this is the first time this user logs in
			try:
				user = User.objects.get(username=auth_info['openid'])

				# auth_info['user'] = user
				# wx_auth = WeixinAuth.objects.create(**auth_info)
				# user_profile = settings.TEST_USER_PROFILE
				# user_profile['user'] = user
				# wx_profile = WeixinProfile.objects.create(**user_profile)

			except User.DoesNotExist:
				# get user profile from Weixin
				# api = WeixinAPI(access_toke=auth_info['access_token'])
				# user_profile = api.user(openid=auth_info['openid'])
				user_profile = settings.TEST_USER_PROFILE

				# create user using openid only and add it to django's User model
				# password is not set (set_unusable_password() when it's not provided)

				user = User.objects.create_user(username=auth_info['openid'], password=settings.WEIXIN_LOGIN_PASSWORD)
				# user.save()

				# add auth_info to WeixinAuth model
				# auth_info keys: access_token, expire_in, refresh_token, openid, scope
				auth_info['user'] = user
				wx_auth = WeixinAuth.objects.create(**auth_info)

				# add user_profile to WeixinProfile models
				# user_profile keys: openid, nickname, sex, province, city, country, headimgurl, privilege, unionid
				user_profile['user'] = user
				wx_profile = WeixinProfile.objects.create(**user_profile)

				# authenticate the user bofere login as the manual suggests


			# log user in.
			# authenticate the user bofere login as the manual suggests
			auth_user = authenticate(username=user.username, password=settings.WEIXIN_LOGIN_PASSWORD)
			login(self.request, auth_user)

			# direct to homepage with personal info
			url = reverse('accounts:login-success')


		return url

class LoginSuccess(TemplateView):
	template_name = 'accounts/login_success.html'

class Logout(RedirectView):

	def get_redirect_url(self, *args, **kwargs):
		url = reverse('accounts:login')
		logout(self.request)
		return url