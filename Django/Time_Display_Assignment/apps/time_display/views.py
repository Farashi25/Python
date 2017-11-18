# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from time import localtime, strftime
from django.utils.crypto import get_random_string


def index(request):
    context = {
    "date": strftime("%b %d, %Y", localtime()), "time": strftime("%-I:%M %p",localtime())
    }
    return render(request, 'time_display/index.html', context)
# Create your views here.
