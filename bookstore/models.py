# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# imported so we can utilize named urls in urls.py
from django.urls import reverse

class Item(models.Model):#Done
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(max_length=255)
    owner = models.ForeignKey(User, related_name="owned_items")

    def get_absolute_url(self):
        return reverse('item_view', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Category(models.Model):#Done
    name = models.CharField(max_length=255)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('update_category', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class ItemRequest(models.Model):
    item = models.ForeignKey(Item, related_name="requests")
    requestor = models.ForeignKey(User, related_name="requested_items")
    request_date = models.DateTimeField(auto_now_add=True)
    request_complete = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('update_item_request', kwargs={'pk': self.pk})

    def __str__(self):
        return self.item.title


class ItemCategory(models.Model):#Done
    item = models.ForeignKey(Item, related_name="catetories")
    category = models.ForeignKey(Category, related_name="categorized_items")
