# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView

from .models import Item

# Create your views here.
from django.http import HttpResponse


# Shane: use generics...
class HomeView(TemplateView):
    template_name='home.html'

class ItemDetail(DetailView):
	model=Item
	template_name='item_detail.html'


