from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import WeixinAuth, WeixinProfile, TiexinProfile
# Register your models here.
admin.site.register(Permission)
admin.site.register(WeixinAuth)
admin.site.register(WeixinProfile)
admin.site.register(TiexinProfile)