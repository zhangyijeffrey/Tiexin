from django.shortcuts import render
from django.http import HttpResponse
from django.generic.views import TemplateView

# Create your views here.
def login_success(request):
		return HttpResponse("You're logged in as %s." % request.user)

class login_success(TemplateView):
	template_name = "login_success.html"
