# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Assets.models import Laptops, Owner, Personals

admin.site.register(Laptops)
admin.site.register(Personals)
admin.site.register(Owner)
