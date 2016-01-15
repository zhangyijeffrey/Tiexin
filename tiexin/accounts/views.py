from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, RedirectView
from weixin.client import WeixinAPI
from tiexin.settings import dev
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout


# Create your views here.
class Login(TemplateView):
	template_name = 'accounts/login.html'

class LoginWeixin(RedirectView):

	def get_redirect_url(self, *args, **kwargs):
		user = self.request.user

		url = reverse('accounts:login-success')
		
		# if user.is_authenticated():
		# 	url = reverse('account:login')
		# else:
		# 	redirect_uri = 
		# 	scope = ('snsapi_login',)
		# 	api = WeixinAPI(appid=APP_ID, app_secret=APP_SECRET, redirect_uri=redirect_uri)
		# 	url = api.get_authorize_url(scope=scope)

		return url


class LoginSuccess(TemplateView):
	template_name = 'accounts/login_success.html'

class Logout(RedirectView):

	def get_redirect_url(self, *args, **kwargs):
		url = reverse('accounts:login')
		logout(self.request)
		return url