from django.conf.urls import url
# from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy


app_name = 'toys'

urlpatterns = [
	# url(r'^$', views.BrowseAllToys.as_view(), name='browse'),
	url(r'^sell/$', views.UserSellAToy.as_view(), name='sell'),
	url(r'^sell/confirm/$', RedirectView.as_view(url=reverse_lazy('toys:sell')), name="sell-confirm"),
	url(r'^sell/confirm/(?P<toy_source_uuid>.+)/$', views.UserSellConfirm.as_view()),
	url(r'^sell/update/$', RedirectView.as_view(url=reverse_lazy('toys:sell')), name="sell-update"),
	url(r'^sell/update/(?P<toy_source_uuid>.+)/$', views.UserUpdateAToy.as_view()),
	url(r'^sell/success/$', TemplateView.as_view(template_name='toys/sell_success.html'), name='sell-success'),
	url(r'^sell/fail/$', TemplateView.as_view(template_name='toys/sell_fail.html'), name='sell-fail'),

	url(r'^receive-and-approve/(?P<toy_source_id>\d+)$', views.ReceiveAndApprove.as_view(), name='receive-and-approve'),
	# url(r'^add-to-inventory/$', views.AddToInventory.as_view(), name='add-to-inventory'),
	url(r'^add-permission/$', views.AddPermission.as_view()),
	url(r'^remove-permission/$', views.RemovePermission.as_view()),
	url(r'^browse/$', views.BrowseAllToys.as_view(), name='browse'),
	# url(r'^update/(?P<pk>\d+)/$', views.UpdateAToy.as_view(), name='update'),
	# url(r'^update-success/$', views.UpdateAToySuccess.as_view(), name='update-success'),
	# url(r'^delete/(?P<pk>\d+)/$', views.DeleteAToy.as_view(), name='delete'),
	# url(r'^delete-success/$', views.DeleteAToySuccess.as_view(), name='delete-success'),
]