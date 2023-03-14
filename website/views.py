from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from entries.models import Entry

# Create your views here.
def splash(request):
    return render(request, "website/splash.html")

def welcome(request):
    return render(request, "website/welcome.html")

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("This will be a page describing what this writers journal is for")