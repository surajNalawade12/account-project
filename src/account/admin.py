# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Account, Employee


admin.site.register(Account)
admin.site.register(Employee)