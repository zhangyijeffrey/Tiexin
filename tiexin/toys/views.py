 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView, CreateView, DeleteView, UpdateView, ListView, DetailView, FormView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import SellAToyForm, UpdateAToyForm, UserSellAToyForm, ReceiveAndApproveForm
from django.contrib.auth.models import User
from .models import Toy, ToySource
from accounts.models import TiexinProfile
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
import re
from django.db.models import Q
from django.conf import settings
from datetime import datetime, timedelta
import pytz
import os
import StringIO
from django.core.files.base import ContentFile
try:
	from PIL import Image
except ImportError:
	import Image
from django.http import Http404

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Create your views here.

class UserSellAToy(LoginRequiredMixin, CreateView):
	# login required mixin
	login_url = reverse_lazy('accounts:login')
	# default: redirect_field_name = 'next'

	# create view
	form_class = UserSellAToyForm
	template_name = 'toys/user_sell_a_toy.html'
	success_url = 'confirm/'


	def get(self, request, *args, **kwargs):
		form = UserSellAToyForm()
		return self.render_to_response(self.get_context_data(form=form))

	def post(self, request, *args, **kwargs):

		if 'cancel' in request.POST:
			return self.get(request, *args, **kwargs)

		form = UserSellAToyForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			print 'it is valid'
			new_toy = form.save(commit=False)

			new_toy.seller = request.user
			new_toy.submit_date = datetime.now(pytz.timezone(settings.TIME_ZONE))

			new_toy.status = '用户提交玩具信息'
			new_toy.status_last_modified = datetime.now(pytz.timezone(settings.TIME_ZONE))

			new_toy.num_images = len(request.FILES)
			estimate_instant_quote(new_toy)
			handle_upload_images_and_save_toy(new_toy, request.FILES)
			new_toy.save()
			success_url = self.success_url + new_toy.uuid
			return HttpResponseRedirect(success_url)
		else:
			print 'it is not valid'
			return self.form_invalid(form=form)

	def get_context_data(self, **kwargs):
		self.object = None
		context = super(UserSellAToy, self).get_context_data(**kwargs)
		return context

def estimate_instant_quote(toy):
	if toy.original_cost:
		toy.instant_quote_point = 100
	else:
		toy.instant_quote_discount = 0.8

def handle_upload_images_and_save_toy(toy, files):
	FULLSIZE_SIZE = 1920
	THUMBNAIL_SIZE = 200
	MAX_IMAGE_NUM = 5

	n_images = toy.num_images
	current_image_ind = 0
	complete_flag = False

	for i in xrange(MAX_IMAGE_NUM):
		# break the loop if all images have been handled
		if current_image_ind == n_images:
			break;

		# upload_filename is the name used in html
		upload_filename = 'image' + str(i+1)
		if upload_filename in files:
			current_image_ind += 1
			while getattr(toy, 'image' + str(current_image_ind)):
				current_image_ind +=1
				if current_image_ind > n_images:
					complete_flag = True
					break;
			if complete_flag:
				break;
		else:
			continue;



		# img is the actual user uploaded file and name
		img = files[upload_filename]
		# split filename and ext to make filename for thumbnail
		filename, file_ext = os.path.splitext(img.name)
		fullsize_name = img.name
		thumbnail_name = filename + '_thumbnail' + file_ext
		print fullsize_name


		# database column name
		fullsize_fieldname = 'image' + str(current_image_ind)
		thumbnail_fieldname = fullsize_fieldname + '_thumbnail'

		# open image file
		image = Image.open(img)
		if image.mode not in ('L', 'RGB'):
			image = image.convert('RGB')
		# resize the raw file to fullsize 
		fullsize_io = StringIO.StringIO()
		image.thumbnail((FULLSIZE_SIZE, FULLSIZE_SIZE), Image.ANTIALIAS)
		image.save(fullsize_io, 'jpeg')
		fullsize_file = ContentFile(fullsize_io.getvalue())
		getattr(toy, fullsize_fieldname).save(fullsize_name, fullsize_file, save=False)

		# resize to thumbnail size
		thumbnail_io = StringIO.StringIO()
		image.thumbnail((THUMBNAIL_SIZE,THUMBNAIL_SIZE), Image.ANTIALIAS)
		image.save(thumbnail_io, 'jpeg')
		thumbnail_file = ContentFile(thumbnail_io.getvalue())
		getattr(toy, thumbnail_fieldname).save(thumbnail_name, thumbnail_file, save=False)

	return

class UserSellConfirm(LoginRequiredMixin, ListView):
	context_object_name = 'toy'
	success_url = reverse_lazy('toys:sell-success')
	fail_url = reverse_lazy('toys:sell-fail')
	template_name = 'toys/user_sell_confirm.html'

	def get(self, request, *args, **kwargs):
		self.object_list = self.get_queryset()
		if self.object_list is None:
			return HttpResponseRedirect(self.fail_url)
		else:
			context = self.get_context_data()
			return self.render_to_response(context)

	def post(self, request, *args, **kwargs):
		toy = self.get_queryset();
		if toy is None:
			return HttpResponseRedirect(self.fail_url)

		if 'cancel' in request.POST:
			toy.is_instant_quote_accepted = False
			toy.status = "用户拒绝估价"
			toy.status_last_modified = datetime.now(pytz.timezone(settings.TIME_ZONE))
			toy.save()
			return HttpResponseRedirect(self.fail_url)
		else:
			if 'user-cell' in request.POST:
				user_cell = request.POST['user-cell']
				if user_cell != '' and re.match('^[ ]+', user_cell) is None:
					try:
						tx_profile = request.user.tiexinprofile
					except TiexinProfile.DoesNotExist:
						tx_profile = TiexinProfile.objects.create(user=request.user)
					tx_profile.cell = request.POST['user-cell']
					tx_profile.save()

			toy.is_instant_quote_accepted = True
			toy.status = "用户接受估价"
			toy.status_last_modified = datetime.now(pytz.timezone(settings.TIME_ZONE))
			toy.save()
			return HttpResponseRedirect(self.success_url)


	def get_queryset(self):
		if self.queryset is None:
			try: 
				self.queryset = ToySource.objects.get(uuid=self.kwargs['toy_source_uuid'])
			except ToySource.DoesNotExist:
				self.queryset = None
		return self.queryset

	def get_context_data(self, **kwargs):
		context = super(UserSellConfirm, self).get_context_data(**kwargs)
		try: 
			user_cell = self.request.user.tiexinprofile.cell
		except TiexinProfile.DoesNotExist:
			user_cell = ''

		context['user_cell'] = user_cell
		return context

class UserUpdateAToy(LoginRequiredMixin, UpdateView):
	# login required mixin
	login_url = reverse_lazy('accounts:login')

	# Update view
	form_class = UserSellAToyForm
	model = ToySource
	pk_url_kwarg = 'uuid'
	template_name = 'toys/user_update_a_toy.html'

	def get_object(self, queryset=None):
		obj = ToySource.objects.get(uuid=self.kwargs['toy_source_uuid'])
		self.queryset = obj
		return obj

	def get_success_url(self):
		return reverse_lazy('toys:sell-confirm')+self.kwargs['toy_source_uuid']

	def post(self, request, *args, **kwargs):

		if 'cancel' in request.POST:
			return self.get(request, *args, **kwargs)

		toy = self.get_object()
		form = UserSellAToyForm(request.POST or None, request.FILES or None, instance=toy)
		if form.is_valid():
			form.save(commit=False)
			toy.status = '用户更改玩具信息'
			status_last_modified = datetime.now(pytz.timezone(settings.TIME_ZONE))

			toy.num_images += len(request.FILES)
			handle_upload_images_and_save_toy(toy, request.FILES)
			toy.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.form_invalid(form=form)

	def get_context_data(self, **kwargs):
		context = super(UserUpdateAToy,self).get_context_data(**kwargs)
		toy = self.queryset
		image_urls = []

		for i in xrange(toy.num_images):
			model_fieldname = 'image'+str(i+1)+'_thumbnail'
			field = getattr(toy, model_fieldname)
			if field:
				image_urls.append(field.url)

		context['image_urls'] = image_urls
		return context

class ReceiveAndApprove(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	login_url = reverse_lazy('accounts:login')
	permission_required = 'toys.approve_toy'

	success_url = reverse_lazy('toys:approve-success')

	context_object_name = 'toy'
	template_name = 'toys/receive_and_approve.html'

	form_class = ReceiveAndApproveForm
	model = ToySource

	def get_object(self, queryset=None):
		obj = ToySource.objects.get(id=self.kwargs['toy_source_id'])
		self.queryset = obj
		return obj

class AddPermission(TemplateView):
	template_name = 'toys/add_permission.html'

	def get_context_data(self, **kwargs):
		context = super(AddPermission, self).get_context_data()
		content_type = ContentType.objects.get_for_model(ToySource)
		permission = Permission.objects.get(content_type=content_type, codename='approve_toy')
		self.request.user.user_permissions.add(permission)
		user = User.objects.filter(id=self.request.user.id)[0]
		print user.has_perm('toys.approve_toy')
		return context

class RemovePermission(TemplateView):
	template_name = 'toys/remove_permission.html'

	def get_context_data(self, **kwargs):
		context = super(RemovePermission, self).get_context_data()
		content_type = ContentType.objects.get_for_model(ToySource)
		permission = Permission.objects.get(content_type=content_type, codename='approve_toy')
		self.request.user.user_permissions.remove(permission)
		user = User.objects.filter(id=self.request.user.id)[0]
		print user.has_perm('toys.approve_toy')
		return context

class BrowseAllToys(ListView):
	model = ToySource
	ordering = '-submit_date'
	template_name = 'toys/browse_all_toys.html'
	context_object_name = 'toys'
	paginate_by = 12

	def get_queryset(self):
		query_string = self.request.GET.get('query', '')
		if query_string == '':
			queryset = self.model.objects.all().order_by(self.get_ordering())
		else:
			query = None
			terms = normalize_query(query_string)
			search_fields = ['title', 'brand', 'description', 'seller']
			for term in terms:
				or_query = None # Query to search for a given term in each filed
				for field_name in search_fields:
					if field_name == 'seller':
						q = Q(**{'seller__weixinprofile__nickname__contains': term})
					else:
						q = Q(**{'%s__contains' % field_name: term})
					if or_query is None:
						or_query = q
					else:
						or_query = or_query | q

				if query is None:
					query = or_query
				else:
					query = query & or_query
			queryset = self.model.objects.filter(query).order_by(self.get_ordering())

		return queryset

	def get_context_data(self, **kwargs):
		context = super(BrowseAllToys, self).get_context_data(**kwargs)
		context['query_string'] = self.request.GET.get('query', '')
		return context




