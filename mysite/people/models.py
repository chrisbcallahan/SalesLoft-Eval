# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class People(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email_address = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
