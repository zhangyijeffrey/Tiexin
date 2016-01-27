from django.conf.urls import url
# from django.contrib.auth import views as auth_views
from . import views

app_name = 'mywishes'

urlpatterns = [
	url(r'^$', views.BrowseAllWishes.as_view(), name='browse'),
	url(r'^create/$', views.CreateAWish.as_view(), name='create'),
	url(r'^create-success/$', views.CreateAWishSuccess.as_view(), name='create-success'),
	url(r'^update/(?P<pk>\d+)/$', views.UpdateAWish.as_view(), name='update'),
	url(r'^update-success/$', views.UpdateAWishSuccess.as_view(), name='update-success'),
	url(r'^delete/(?P<pk>\d+)/$', views.DeleteAWish.as_view(), name='delete'),
	url(r'^delete-success/$', views.DeleteAWishSuccess.as_view(), name='delete-success'),
]