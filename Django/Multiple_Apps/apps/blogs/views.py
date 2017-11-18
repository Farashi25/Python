# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.shortcuts import render,HttpResponse, redirect
# from django.contrib import messages
# from time import gmtime, strftime
# from django.utils.crypto import get_random_string
#
#
# def index(request):
#     if not 'count' in request.session:
#         request.session['count'] = 1
#     context = {
#         'string' : get_random_string(length = 14),
#
#     }
#     return render (request, 'random_words_generator/index.html',context)
#
#
# def process(request):
#     request.session['count'] += 1
#     return redirect('/')
#
# def reset(request):
#     del request.session['count']
#     return redirect('/')










# def index(request):
#     context = {
#         "email" : "blog@gmail.com",
#         "name" : "mike"
#     }
#     return render(request, "blogs/index.html", context)
#
#
# def create(request):
#     if request.method == "POST":
#         print "*"*50
#         print request.POST
#         print request.POST['name']
#         print request.POST['desc']
#         resquest.session['name'] = "test"
#         print "*"*50
#         return redirect("/")
#     else:
#         return redirect("/")
#



# def create(request):
# 	if request.method == "POST":
#         print "*"*50
#         print request.POST
#         print request.POST['name']
#         print request.POST['desc']
#         request.session['name'] = "test"  # more on session below
#         "*"*50
#         return redirect("/")
# 	else:
# 		return redirect("/")

def index(request):
    response = "Hello, I am your second request"
    return HttpResponse(response)

def new(request):
    response = "Hello, I am your third request"
    return HttpResponse(response)

def create(request):
    response = "Hello, I am your fourth request"
    return redirect  ('/blogs')

def show(request, number):
    response = "Hello, I am a number"
    return HttpResponse(response)

def edit(request, number):
    response = "Hello, I am a editable{}" '' .format(number)
    return HttpResponse(response)

def destroy(request, number):
    print  "Hello, I am a destroyer"
    return redirect  ('/blogs')

# Create your views here.
