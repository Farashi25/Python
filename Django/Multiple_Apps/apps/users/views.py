# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string


def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "users/index.html", context)



def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        resquest.session['name'] = "test"
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")

# def index(request):
#     response = "Hello, I am your second request"
#     return HttpResponse(response)
#
# def register(request):
#     response = "Hello, I am your third request"
#     return HttpResponse(response)
#
# def login(request):
#     response = "Hello, I am your fourth request"
#     return redirect  ('/users')

# def show(request, number):
#     response = "Hello, I am a number"
#     return HttpResponse(response)
#
# def edit(request, number):
#     response = "Hello, I am a editable{}" '' .format(number)
#     return HttpResponse(response)
#
# def destroy(request, number):
#     print  "Hello, I am a destroyer"
#     return redirect  ('/blogs')
# Create your views here.
