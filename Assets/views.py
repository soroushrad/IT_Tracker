# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from httplib import HTTPResponse
from urllib2 import HTTPRedirectHandler

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.serializers import json
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from pip._vendor.urllib3 import HTTPResponse

from Assets.models import Laptops, Personals, Owner


def tables_laptop_view(request):
    if request.user.is_authenticated:
        auth_user = request.user
        laptops = Laptops.objects.all()
        laptops_context = {

            'laptops': laptops,
            'auth_user': auth_user
        }
        return render(request, 'laptops_tables.html', context=laptops_context)
    else:
        return render(request, '404_not_found.html')


def tables_staffs_view(request):
    if request.user.is_authenticated:
        auth_user = request.user
        staffs = Personals.objects.all()
        staffs_context = {
            'staffs': staffs,
            'auth_user': auth_user
        }
        return render(request, 'Staffs_tables.html', context=staffs_context)
    else:
        return render(request, '404_not_found.html')


@login_required
def dashboard_view(request):
    auth_user = request.user
    staffs = Personals.objects.all()
    staffs_len = len(staffs)
    laptop_all = Laptops.objects.all()
    laptop_st_1 = Laptops.objects.filter(Laptop_status=1)
    laptop_st_2 = Laptops.objects.filter(Laptop_status=2)
    laptop_st_3 = Laptops.objects.filter(Laptop_status=3)
    laptop_st_4 = Laptops.objects.filter(Laptop_status=4)
    laptop_st_1_len = len(laptop_st_1)
    laptop_st_2_len = len(laptop_st_2)
    laptop_st_3_len = len(laptop_st_3)
    laptop_st_4_len = len(laptop_st_4)
    laptop_st_total_count = {
        'laptop_st_1_count': laptop_st_1_len,
        'laptop_st_2_count': laptop_st_2_len,
        'laptop_st_3_count': laptop_st_3_len,
        'laptop_st_4_count': laptop_st_4_len,
        'staffs_len': staffs_len,
        'laptops': laptop_all,
        'auth_user': auth_user,
    }

    return render(request, 'dashboard.html', context=laptop_st_total_count)


def tables_owners_view(request):
    if request.user.is_authenticated:
        auth_user = request.user
        owner = Owner.objects.all()
        owner_context = {
            'owners': owner,
            'auth_user': auth_user
        }
        return render(request, 'Owners_tables.html', owner_context)
    else:
        return render(request, '404_not_found.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise Http404("User or Password is incorrect Please try again")
        else:
            login(request, user)
            return redirect('dashboard_view')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request, 'log_out_successfully.html')
