from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
	url(r'^login/$', views.Login.as_view(), name='login'),
	url(r'^login-weixin/$', views.LoginWeixin.as_view(), name='login-weixin' ),
	url(r'^weixin-auth/$', views.WeixinAuth.as_view(), name='weixin-auth'),
	url(r'^login-success/$', views.LoginSuccess.as_view(), name='login-success'),
	url(r'^logout/$', views.Logout.as_view(), name='logout'),
]