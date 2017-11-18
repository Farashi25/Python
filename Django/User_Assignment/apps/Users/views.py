# -*- coding: utf-8 -*
from django.shortcuts import render,redirect
from models import Users
# Create your views here.
def index(request):
    return render(request, 'index.html')
