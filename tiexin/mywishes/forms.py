 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from django import forms
from models import Wish

class WishForm(forms.ModelForm):
	class Meta:
		model = Wish
		fields = ('title', 'time', 'location', 'content')
		labels = {
			'title': '题目',
			'time': '活动时间',
			'location': '活动地点',
			'content': '内容',
		}
		error_message = {
			'title':{
				'max_length': "题目过长"
			}
		}
