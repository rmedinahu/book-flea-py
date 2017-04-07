# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(max_length=255)
    owner = models.ForeignKey(User, related_name="owned_items")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class ItemRequest(models.Model):
    item = models.ForeignKey(Item, related_name="requests")
    requestor = models.ForeignKey(User, related_name="requested_items")
    request_date = models.DateTimeField(auto_now_add=True)
    request_complete = models.BooleanField(default=False)


    def __str__(self):
        return self.item


class ItemCategory(models.Model):
    item = models.ForeignKey(Item, related_name="catetories")
    category = models.ForeignKey(Category, related_name="categorized_items")


 

