# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    return render(request,'survey_form/index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['lang'] = request.POST['lang']
    request.session['location'] = request.POST['location']
    request.session['comment'] = request.POST['comment']
    if not 'number' in request.session:
        request.session['number'] = 1
    else:
        request.session['number'] += 1
    return redirect('/result')

def result(request):
    return render(request,'survey_form/result.html')
