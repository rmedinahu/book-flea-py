# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, FormView


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

class CreateItemRequestView(CreateView):
    model = ItemRequest
    template_name = 'itemrequestview.html'
    fields = ['item', 'requestor', 'request_complete']

class SearchForm(forms.Form):
    search = forms.CharField()
    
class SearchSystem(FormView):
    template_name = 'searchsystem.html'
    form_class = SearchForm

    def form_valid(self, form):
        context = self.get_context_data()
        books = form.cleaned_data['search']
        context['results'] = Item.objects.filter(title__contains=books)
        return render(self.request, self.template_name, context)