from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
	url(r'^login/$', views.Login.as_view(), name='login'),
	url(r'^login-weixin/$', views.LoginWeixin.as_view(), name='login-weixin' ),
	url(r'^auth-weixin/$', views.AuthWeixin.as_view(), name='auth-weixin'),
	url(r'^login-success/$', views.LoginSuccess.as_view(), name='login-success'),
	url(r'^logout/$', views.Logout.as_view(), name='logout'),
]