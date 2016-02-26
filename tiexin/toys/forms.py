 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from django import forms
from models import Toy, ToySource

class SellAToyForm(forms.ModelForm):
	class Meta:
		model = Toy
		fields = ['title', 'description', 'brand', 'sold_by_propose_price']
		# fields = ['title', 'description', 'brand', 'sold_by_propose_price']

		labels = {
			'title': "产品名称",
			'description': "描述",
			'brand': "品牌",
			'sold_by_propose_price': "提议价格",
		 }

		widgets = {
		 	'title': forms.TextInput(attrs={'class': 'form-control'}),
		 	'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '6'}),
			'brand': forms.TextInput(attrs={'class': 'form-control'}),
			'sold_by_propose_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
		 }


class UpdateAToyForm(forms.ModelForm):
	class Meta:
		model = Toy
		fields = ['title', 'status', 'description', 'brand', 'sold_by', 'sold_by_propose_time',  'sold_by_propose_price', 'sold_by_accept_time', 'sold_by_accept_price', 'sell_price', 'publish_time']

EMPTY_CHOICE = ('', '------')

def make_choices(choice_list):
	choices = (EMPTY_CHOICE, )
	for choice in choice_list:
		choices += ((choice, choice),)
	return choices

HAS_ORIGINAL_RECEIPT_CHOICES = make_choices(['有', '没有'])
PURCHASE_TIME_CHOICES = make_choices(['一个月以内', '三个月以内', '六个月以内', '一年以内', '两年以内', '三年以内', '三年以上'])
EXTERIOR_CHOICES  = make_choices(['全新未拆封','外观完好','外观有轻微损伤或褪色','外观有明显损伤'])
FUNCTIONALITY_CHOICES = make_choices(['功能正常', '缺失非功能性配件', '无法正常使用'])

class UserSellAToyForm(forms.ModelForm):
	class Meta:
		model = ToySource
		fields = ['title', 'brand', 'original_cost', 'original_vendor','has_original_receipt', 'purchase_time', 'exterior', 'functionality','description']

		labels = {
			'title': '产品名称',
			'brand': '品牌',
			'original_cost': '购买价格',
			'original_vendor': '购买途径',
			'has_original_receipt': '购买票据',
			'purchase_time': '购买时间',
			'exterior': '外观',
			'functionality': '功能',
			'description': '补充描述',
		 }

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'brand': forms.TextInput(attrs={'class': 'form-control'}),
			'original_cost': forms.NumberInput(attrs={'class': 'form-control','step':'1'}),
			'original_vendor': forms.TextInput(attrs={'class': 'form-control'}),
			'has_original_receipt': forms.Select(choices=HAS_ORIGINAL_RECEIPT_CHOICES, attrs={'class': 'form-control'}),
			'purchase_time': forms.Select(choices=PURCHASE_TIME_CHOICES, attrs={'class': 'form-control'}),
			'exterior': forms.Select(choices=EXTERIOR_CHOICES, attrs={'class': 'form-control'}),
			'functionality': forms.Select(choices=FUNCTIONALITY_CHOICES, attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
		 }