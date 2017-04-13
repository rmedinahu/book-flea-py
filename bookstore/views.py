# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.views.generic import TemplateView, DetailView, ListView, UpdateView, CreateView

from .models import Item

# Create your views here.
from django.http import HttpResponse

# Shane: use generics...
class HomeView(TemplateView):
    template_name='home.html'

class UpdateBookView(UpdateView):
    model = Item
    template_name ='update.html'
    fields = ['title', 'category', 'price', 'description', 'owner']

class ItemCreateView(CreateView):
    """ Show a page containing a form for adding a new Item object.
    url pattern: /item/add name: item_add
    """
    model = Item
    template_name = 'item_create.html'
    fields = ['title', 'category', 'price', 'description', 'owner']

