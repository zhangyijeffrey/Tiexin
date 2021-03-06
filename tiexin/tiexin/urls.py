"""tiexin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='accounts/login')),
	url(r'^accounts/', include('accounts.urls', namespace='accounts')),
	url(r'^mywishes/', include('mywishes.urls', namespace='mywishes')),
    url(r'^toys/', include('toys.urls', namespace='toys')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
