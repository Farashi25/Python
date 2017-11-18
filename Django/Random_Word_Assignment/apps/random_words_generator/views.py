# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string


def index(request):
    if not 'count' in request.session:
        request.session['count'] = 1
    context = {
        'string' : get_random_string(length = 14),

    }
    return render (request, 'random_words_generator/index.html',context)


def process(request):
    request.session['count'] += 1
    return redirect('/')

def reset(request):
    del request.session['count']
    return redirect('/')
# Create your views here.
