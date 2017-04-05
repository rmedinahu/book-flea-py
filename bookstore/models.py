# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    userID = models.IntegerField()
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

class Item(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(User)
