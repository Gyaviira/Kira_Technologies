from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

def index(request):
    return HttpResponse("This works!!")