from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
	url(r'^login/$', auth_views.login, name='login', kwargs={'template_name': 'accounts/login.html'}),
	url(r'^login/success/$', views.login_success.as_view()),
	url(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': 'accounts:login'}),
]