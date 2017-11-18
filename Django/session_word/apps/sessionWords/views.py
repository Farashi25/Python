# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import datetime
# Create your views here.
def index(request):
    print datetime.now()
    return render( request, "sessionWords/index.html")

def addword(request):
    request.session.modified = True
    if 'stored_words' not in request.session:
        request.session['stored_words'] = []
    if 'big' in request.POST:
        data = {
            "word" : request.POST['word'],
            "color" : request.POST['color'],
            "size" : "big",
            "time" : datetime.now().strftime("%-I:%M:%S %p - %B %d %Y")
            }
        request.session['stored_words'].append(data)
    else:
        data = {
            "word" : request.POST['word'],
            "color" : request.POST['color'],
            "size" : "small",
            "time" :  datetime.now().strftime("%-I:%M:%S %p - %B %d %Y")
            }
        request.session['stored_words'].append(data)
    return redirect("/")
