# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Item, Category, ItemRequest, ItemCategory


admin.site.register(Item)
admin.site.register(Category)
admin.site.register(ItemRequest)
admin.site.register(ItemCategory)