from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.urls import reverse


monhtly_challenges = {
    "january":" Tulya miyeembe",
    "February":" Tulye enkoko",
    "march":" Tulya chips",
    "april":" Tulya papaali",
    "may":" Tulya fene",
    "june":" Tulya muwogo",
    "july":" Tutambula nnyo",
    "october":" Tunwa chai muzuri",
    "september":" Tukola duyilo",
    "november":" Tuduka misinde",
    "december":" Tulya mpuuta"
 }

def monthly_challenge_by_number(request, month):
    months = list(monhtly_challenges.keys())
    if month >len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_month])
    return HttpResponse(redirect_path)

def monthly_challenge(request,month):
    try:
        challenge_text = monhtly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
    

def home(request):
    return render(request,'blog/home.html')

def index(request):
    return render(request,'blog/index.html')

def residence(request):
    return HttpResponse('Gayaza')

def user(request):
    return HttpResponse('mayanja')