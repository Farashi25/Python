# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from models import User, UserManager
import bcrypt


def index(request):
    return render(request, 'index.html')


def login(request):
    errors = User.objects.loginvalidator(request.POST)
    if len(errors):
        for tag,error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        request.session['name'] = User.objects.get(email=request.POST['email']).first_name
        return redirect('/success')


def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag,error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else:
        pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email = request.POST['email'], password = pwhash)
        request.session['name'] = request.POST['fname']
        return redirect('/success')
    return redirect('/')



def success(request):
    return render(request, 'success.html')
