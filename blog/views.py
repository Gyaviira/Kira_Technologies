from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'blog/home.html')

def residence(request):
    return HttpResponse('Gayaza')
def index(request):
    return HttpResponse('Kira')
def user(request):
    return HttpResponse('mayanja')