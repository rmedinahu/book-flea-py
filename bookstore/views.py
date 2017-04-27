# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView


from .models import Item, Category, ItemCategory, ItemRequest

# Create your views here.
from django.http import HttpResponse

# Shane: use generics...
class HomeView(TemplateView):
    template_name='home.html'

class ItemDetail(DetailView):
	model=Item
	template_name='item_detail.html'

class ItemCategoryView(CreateView):
	model = Category
	template_name = 'item_category.html'
	fields = ['name','description']

class UpdateItemCategoryView(UpdateView):
    model = Category
    template_name = 'update_category.html'
    fields = ['name', 'description']

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

class DetailItemCategoryView(DetailView):
    model = ItemCategory
    template_name = 'detail_item_category.html'
    fields = ['item', 'category']

class CategoryDetailView(DetailView):
    model= Category
    template_name='category_view.html'

class CreateItemCategoryView(CreateView):
    model = ItemCategory
    template_name = 'createitem_category.html'
    fields = ['item', 'category']

class DetailItemRequestView(DetailView):
    model = ItemRequest
    template_name = 'detail_item_request.html'
    fields = ['item', 'requestor']
