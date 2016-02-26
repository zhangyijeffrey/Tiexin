from django.conf.urls import url
# from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView

app_name = 'toys'

urlpatterns = [
	# url(r'^$', views.BrowseAllToys.as_view(), name='browse'),
	url(r'^sell/$', views.UserSellAToy.as_view(), name='sell'),
	# url(r'^sell/confirm/$', views.UserSellConfirm.as_view(), name="sell-confirm"),
	url(r'^sell/confirm/(?P<toy_source_uuid>.+)/$', views.UserSellConfirm.as_view(), name="sell-confirm"),

	url(r'^sell/success/$', TemplateView.as_view(template_name='toys/sell_success.html'), name='sell-success'),
	url(r'^sell/fail/$', TemplateView.as_view(template_name='toys/sell_fail.html'), name='sell-fail'),
	url(r'^browse/$', views.BrowseAllToys.as_view(), name='browse'),
	# url(r'^update/(?P<pk>\d+)/$', views.UpdateAToy.as_view(), name='update'),
	# url(r'^update-success/$', views.UpdateAToySuccess.as_view(), name='update-success'),
	# url(r'^delete/(?P<pk>\d+)/$', views.DeleteAToy.as_view(), name='delete'),
	# url(r'^delete-success/$', views.DeleteAToySuccess.as_view(), name='delete-success'),
]