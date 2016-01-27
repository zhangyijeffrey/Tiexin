 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView, CreateView, DeleteView, UpdateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import WishForm
from .models import Wish
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
import re
from django.db.models import Q


# Create your views here.
class BrowseAllWishes(ListView):
	template_name = 'mywishes/all-wishes.html'
	context_object_name = 'wishes'
	paginate_by = 4

	def get_queryset(self):
		query_string = self.request.GET.get('query', '')
		if query_string == '':
			queryset = Wish.objects.all().order_by('-publish_time')
		else:
			query = None
			terms = normalize_query(query_string)
			search_fields = ['title', 'proposed_by', 'location', 'content', 'status']
			for term in terms:
				or_query = None # Query to search for a given term in each filed
				for field_name in search_fields:
					if field_name == 'proposed_by':
						q = Q(**{'proposed_by__weixinprofile__nickname__contains': term})
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
			queryset = Wish.objects.filter(query).order_by('-publish_time')

		return queryset

	def get_context_data(self, **kwargs):
		context = super(BrowseAllWishes, self).get_context_data(**kwargs)
		context['query_string'] = self.request.GET.get('query', '')
		return context

class CreateAWish(LoginRequiredMixin, CreateView):
	# login required mixin
	login_url = reverse_lazy('accounts:login')
	# default: redirect_field_name = 'next'

	# create view
	form_class = WishForm
	template_name = 'mywishes/create_a_wish.html'
	success_url = reverse_lazy('mywishes:browse')


	def get(self, request, *args, **kwargs):
		form = WishForm(initial={
			'title': '贴心网',
			'time':'2016-01-01 6:30:30',
			'location': '嘉兴',
			'content': 'We are awesome!'})
		return self.render_to_response(self.get_context_data(form=form))
		# return render(request, self.template_name, {'form': form})


	def post(self, request, *args, **kwargs):
		form = self.get_form()#WishForm(request.POST)
		if form.is_valid():
			print 'it is valid'
			new_wish = form.save(commit=False)
			print request.user
			new_wish.proposed_by = request.user
			new_wish.status = 'Published'
			new_wish.save()
			return HttpResponseRedirect(self.success_url)
		else:
			print 'it is not valid'
			# return HttpResponseRedirect(self.success_url)
			return self.form_invalid(form)

	def get_context_data(self, **kwargs):
		self.object = None
		context = super(CreateAWish, self).get_context_data(**kwargs)
		return context



class CreateAWishSuccess(TemplateView):
	template_name = 'mywishes/create_success.html'

class UpdateAWish(LoginRequiredMixin, UpdateView):
	# login required mixin
	login_url = reverse_lazy('accounts:login')

	# Update view
	form_class = WishForm
	model = Wish
	template_name = 'mywishes/update_a_wish.html'
	success_url = reverse_lazy('mywishes:browse')

class UpdateAWishSuccess(TemplateView):
	template_name = 'mywishes/update_success.html'

class DeleteAWish(LoginRequiredMixin, DeleteView):
	login_url = reverse_lazy('accounts:login')

	model = Wish
	template_name = 'mywishes/delete_a_wish.html'
	success_url = reverse_lazy('mywishes:browse')

	content_object_name = 'wish'


class DeleteAWishSuccess(TemplateView):
	template_name = 'mywishes/delete_success.html'


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 




